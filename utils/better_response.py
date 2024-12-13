from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_response(message):
    prompt =  f"""You are a Discord Bot. You talk in a funny way. 
    You add the exact word at last of each sentence. "Radhekrishna."
    Here is the message you received: {message}
    
    """
    # Use the Groq client to send a message and receive a response
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
        stream=False,
    )

    # Return the content of the first message choice
    return chat_completion.choices[0].message.content

# Initialize the Groq client using API key from environment variables
client = Groq(api_key=GROQ_API_KEY)
