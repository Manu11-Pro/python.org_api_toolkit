import fastapi
import requests

response = requests.get("https://www.python.org/")
print(f"Status: {response.status_code}")