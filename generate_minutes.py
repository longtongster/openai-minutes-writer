from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load your API key from environment or config
client = OpenAI(api_key = os.getenv("OPEN_API_KEY",default="None"))
#print(openai.api_key)

# Load your example and new transcript
with open("examples/example_1_transcript.txt", "r") as f:
    example_transcript = f.read()

with open("examples/example_1_minutes.txt", "r") as f:
    example_minutes = f.read()

with open("transcripts/real_meeting_2025-04-10.txt", "r") as f:
    new_transcript = f.read()

# Construct the full prompt
prompt = f"""
You are a professional meeting assistant who writes clear and concise meeting minutes. Match the tone, format, and structure of the provided example.

## Example Transcript
\"\"\"{example_transcript}\"\"\"

## Example Minutes
{example_minutes}

---

Now, based on the following transcript, write the minutes in the same style.

Meeting Topic: CRM Migration  
Date: April 10, 2025  
Attendees: Anna, Luca, Maria

## Transcript
\"\"\"{new_transcript}\"\"\"
"""

# Call the OpenAI API
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.4
)

# Output the result
print("\nGenerated Minutes:\n")
print(response.choices[0].message.content)
