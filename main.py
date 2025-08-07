import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.run_python import schema_run_python_file, run_python_file
from functions.write_file import schema_write_file, write_file

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

    if verbose:
        args.remove("--verbose")
    
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)
    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

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

    generate_content(
        client, 
        messages, 
        system_prompt, 
        available_function,
        user_prompt, 
        verbose
    )

def generate_content(client, messages, system_prompt, available_functions, user_prompt="", verbose=False):
    config = types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=system_prompt,
    )
    
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=config
    )
    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    function_calls = response.function_calls

    print(f"Calling function: {function_calls[0].name}({function_calls[0].args})")
    print("\nResponse:")
    print(response.text)


if __name__ == "__main__":
    main()
