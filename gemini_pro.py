import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing in .env file")

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_story(outline):

    prompt = f"""
You are ComicCraft, an AI comic story creator.

Create detailed dialogue and narration for a 5-panel comic.

Use this outline:
{outline}

For each panel provide:
- panel
- narration
- dialogue

Return ONLY valid JSON.
"""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    return response.text.strip()