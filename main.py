import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_file_content import schema_get_file_content
from functions.get_files_info import schema_get_files_info
from functions.run_python import schema_run_python_file
from functions.write_file import schema_write_file
from functions.call_function import call_function
from config import MAX_CHAT_LENGTH
from prompt import system_prompt
from model import gemini_model

def main():
    load_dotenv()

    args = sys.argv[1:]

    if not args:
        print("Code AI Agent")
        print("Usage: uv run main.py <your_prompt>")
        print("Example: uv run main.py \"How to build a calculator app?\"")
        print("Use --verbose for detailed output.")
        sys.exit(1)
    
    verbose = "--verbose" in args

    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        user_prompt.remove("--verbose")

    available_function = types.Tool(
        function_declarations=[
            schema_get_file_content,
            schema_get_files_info,
            schema_run_python_file,
            schema_write_file
        ]
    )

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    for i in range(MAX_CHAT_LENGTH):
        try:
            response = generate_content(
                client, 
                messages, 
                available_function,
                verbose
            )
            
            if response.text:
                print(f"\nCode AI Agent: {response.text}")

        except Exception as e:
            print(f"Error: {e}")
            break

def generate_content(client, messages, available_functions, verbose=False):
    config = types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=system_prompt,
    )
    
    response = client.models.generate_content(
        model=gemini_model,
        contents=messages,
        config=config
    )
    
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    for candidate in response.candidates:
        messages.append(candidate.content)


    function_responses = []

    if not response.function_calls:
        return response

    for function_call in response.function_calls:
        function_call_result = call_function(function_call, verbose=verbose)

        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")

        function_responses.append(
            function_call_result.parts[0]
        )

    messages.append(types.Content(role="tool", parts=function_responses))
    
    if not function_responses:
        raise Exception("Error: function call result is empty.")

    final_response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=config
    )

    return final_response


if __name__ == "__main__":
    main()
