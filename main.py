import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def main():
    user_prompt = sys.argv[1] if len(sys.argv) > 1 else None

    if not user_prompt:
        print("Usage: uv run main.py <your_prompt>")
        sys.exit(1)

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=user_prompt
    )

    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
