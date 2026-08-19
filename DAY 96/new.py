import os
import requests
from send_email import send_email

api_key = os.environ["NEWSAPI_KEY"]
url = (
    "https://newsapi.org/v2/everything"
    f"?q=tesla&sortBy=publishedAt&apiKey={api_key}"
)

response = requests.get(url)
response.raise_for_status()
content = response.json()

body = ""
for article in content.get("articles", []):
    title = article.get("title")
    if title:
        description = article.get("description") or ""
        body += f"{title}\n{description}\n\n"

send_email(message=body)