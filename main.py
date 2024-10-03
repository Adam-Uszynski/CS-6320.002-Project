import os
import openai

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    # Prompt the user for input
    user_prompt = input("Please enter your prompt: ")

    # Prepare the messages for the ChatCompletion API
    messages = [
        {"role": "user", "content": user_prompt}
    ]

    try:
        # Call the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
            messages=messages,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )

        # Extract the assistant's reply
        generated_text = response.choices[0].message.content.strip()

        # Display the response
        print("\nGenerated response:")
        print(generated_text)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
