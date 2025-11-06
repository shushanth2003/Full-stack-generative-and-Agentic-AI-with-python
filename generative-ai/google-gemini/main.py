from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv();

client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "You need assist only math related content if the content is not related math content please assist sorry content is not related"},
        {
            "role": "user",
            "content": "Hi, Myself Shushanth"
        }
    ]
)

print(response.choices[0].message)