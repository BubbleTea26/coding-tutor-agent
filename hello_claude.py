"""hello_claude.py — first Claude API call from Python."""

import os
from dotenv import load_dotenv
from anthropic import Anthropic

# Load variables from .env into the process's environment
load_dotenv()

# Create the API client. It auto-reads ANTHROPIC_API_KEY from env vars.
client = Anthropic()

# Send a single message; get a single response.
response = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=300,
    messages=[
        {
            "role": "user",
            "content": "Hello! In 2-3 sentences, what makes Python a good first language to learn?",
        }
    ],
)

# response.content is a list of content blocks; for plain text replies
# the first block has the text we want.
print(response.content[0].text)