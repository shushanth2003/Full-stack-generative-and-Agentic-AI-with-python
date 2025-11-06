from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv();

client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
SYSTEM_PROMPT="You need to assist only coding in this session if someone asked about irrelated about coding just tell sorry no need any explaination got it"
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content":SYSTEM_PROMPT},
        {
            "role": "user",
            "content": "write the java code for fibonnaci series"
        }
    ]
)

print(response.choices[0].message)