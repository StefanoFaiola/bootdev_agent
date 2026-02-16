import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse


def main():
    parser = argparse.ArgumentParser(description='Chatbot')
    parser.add_argument('user_prompt', type=str, help= "User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("Environment variable not found")




    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    generate_content(client, messages, args.user_prompt, args.verbose)


def generate_content(client, messages, prompt, verbose):
    response = client.models.generate_content(
        model= "gemini-2.5-flash",
        contents= messages)


    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    response_text = response.text

    if verbose:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")
    print(f"Response: \n {response_text}")


if __name__ == "__main__":
    main()
