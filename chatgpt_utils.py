import openai
import os

def set_openai_api_key(api_key: str) -> None:
    """
    Set the OpenAI API key for authentication.
    """
    openai.api_key = api_key

def format_text_with_chatgpt(text: str) -> str:
    """
    Sends the given text to the ChatGPT API with a prompt to reformat it for easier reading.
    Returns the response (formatted text).
    """
    prompt = f"Format this text for easier reading:\n\n{text}"

    # Example with ChatCompletion (GPT-3.5 or GPT-4, etc.)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    formatted_text = response.choices[0].message.content.strip()
    return formatted_text
