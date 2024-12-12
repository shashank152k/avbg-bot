from groq import Groq
import os


def generate_response(message):

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        model="llama3-8b-8192",
        stream=False,
    )

    return chat_completion.choices[0].message.content

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)
