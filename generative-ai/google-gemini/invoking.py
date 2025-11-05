from google import genai
from dotenv import load_dotenv
import os
load_dotenv()

client = genai.Client(
    api_key=os.getenv("API_KEY")
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="what is most valuable skills in 2025",
)

print(response.text)