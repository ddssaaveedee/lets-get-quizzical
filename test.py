"""Initial test file"""

# pylint: disable=E0401
from google.genai.client import Client

from general import load_secrets

secrets = load_secrets()

client = Client(api_key=secrets.get("GEMINI_API_KEY"))

response = client.models.generate_content(model="gemini-2.5-flash", contents="Explain how AI works")
print(response.text)
