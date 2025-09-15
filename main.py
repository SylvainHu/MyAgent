from google import genai
from google.genai import types
import os
import sys
from dotenv import load_dotenv


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        print("Key not set!")
        sys.exit(1)
    client = genai.Client(api_key=api_key)

    if len(sys.argv) == 1:
        print("Please provide a prompt!")
        sys.exit(1)

    args = sys.argv[1:]
    verbose = False
    if "--verbose" in args:
        verbose = True
        args.remove("--verbose")

    user_prompt = " ".join(args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, verbose, user_prompt)

def generate_content(client, messages, verbose, user_prompt):  
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages,
    )

    print(response.text)

    if (verbose):
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")



if __name__ == "__main__":
    main()