
import os
import openai
import argparse
import logging

# Set up logging
logging.basicConfig(filename='openai_responses.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Set your OpenAI API key
def set_api_key(api_key):
    if api_key:
        openai.api_key = api_key
    else:
        openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise ValueError("OpenAI API key not found. Please provide it via the environment variable or --api_key argument.")

def generate_response(user_prompt, model="gpt-3.5-turbo", max_tokens=150, n=1, temperature=0.7, conversation_history=None):
    messages = []
    
    # Include conversation history if provided
    if conversation_history:
        for history_item in conversation_history:
            messages.append({"role": "user", "content": history_item})
    
    messages.append({"role": "user", "content": user_prompt})
    
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            n=n,
            temperature=temperature,
        )
        return [choice.message.content.strip() for choice in response.choices]
    except Exception as e:
        return [f"An error occurred: {e}"]

def main():
    # Argument parser for command-line interaction
    parser = argparse.ArgumentParser(description="OpenAI ChatCompletion Script")
    
    # Adding optional arguments for the API customization and features
    parser.add_argument("--prompt", type=str, help="The prompt to send to the model.")
    parser.add_argument("--input_file", type=str, help="File containing the prompt.")
    parser.add_argument("--output_file", type=str, help="File to save the generated response.")
    parser.add_argument("--model", type=str, default="gpt-3.5-turbo", help="Model to use (default: gpt-3.5-turbo).")
    parser.add_argument("--max_tokens", type=int, default=150, help="Max tokens for the response.")
    parser.add_argument("--n", type=int, default=1, help="Number of responses to generate.")
    parser.add_argument("--temperature", type=float, default=0.7, help="Sampling temperature for generation.")
    parser.add_argument("--api_key", type=str, help="OpenAI API key if not set in the environment.")
    parser.add_argument("--conversation_history", type=str, nargs='*', help="Include previous conversation history.")
    
    args = parser.parse_args()

    # Set API key
    try:
        set_api_key(args.api_key)
    except ValueError as e:
        print(e)
        return
    
    # Handle prompt input from file or command-line
    if args.input_file:
        if os.path.exists(args.input_file):
            with open(args.input_file, 'r') as f:
                user_prompt = f.read().strip()
        else:
            print(f"Input file {args.input_file} does not exist.")
            return
    elif args.prompt:
        user_prompt = args.prompt
    else:
        user_prompt = input("Please enter your prompt: ")
    
    # Generate response(s)
    responses = generate_response(
        user_prompt=user_prompt, 
        model=args.model, 
        max_tokens=args.max_tokens, 
        n=args.n, 
        temperature=args.temperature,
        conversation_history=args.conversation_history
    )
    
    # Print responses and optionally save to file
    print("\nGenerated response(s):")
    for idx, response in enumerate(responses, 1):
        print(f"Response {idx}: {response}")
        # Log each response
        logging.info(f"Prompt: {user_prompt} | Response {idx}: {response}")
    
    if args.output_file:
        with open(args.output_file, 'w') as f:
            for response in responses:
                f.write(response + "\n")
        print(f"Responses saved to {args.output_file}")

if __name__ == "__main__":
    main()
