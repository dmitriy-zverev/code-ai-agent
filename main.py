import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()

    args = sys.argv[1:]

    if not args:
        print("Code AI Agent")
        print("Usage: uv run main.py <your_prompt>")
        print("Example: uv run main.py \"How to build a calculator app?\"")
        sys.exit(1)
    
    verbose = "--verbose" in args

    if verbose:
        args.remove("--verbose")
    
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, user_prompt, verbose)

def generate_content(client, messages, user_prompt="", verbose=False):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )
    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print("\nResponse:")
    print(response.text)


if __name__ == "__main__":
    main()
