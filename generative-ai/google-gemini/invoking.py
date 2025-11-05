from google import genai

client = genai.Client(
    api_key="AIzaSyAAjQ6RnB9vOR077tygqlW-XKs0a61R1Ng"
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="what is most valuable skills in 2025",
)

print(response.text)