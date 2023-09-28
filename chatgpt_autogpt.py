import openai
import os

# Set up OpenAI API credentials
openai.api_key = "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"

# Set up the default Auto-GPT model to use
model = "text-davinci-002"

# Define a function to handle user input
def handle_user_input(input_text):
    if input_text.lower().startswith("write code"):
        code = input_text[10:]
        response = generate_auto_gpt(model, code)
        return "Auto-GPT: " + response
    else:
        return "ChatGPT: I'm sorry, I don't understand. Please try again."

# Define a function to generate a response using Auto-GPT
def generate_auto_gpt(model, prompt):
    completions = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text.strip()
    return message

# Start the chat loop
while True:
    input_text = input(">> ")
    response = handle_user_input(input_text)
    print(response)

