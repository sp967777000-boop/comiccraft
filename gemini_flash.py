import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing in .env file")

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_outline(story_prompt, character_name, setting, tone, art_style):

    prompt = f"""
You are ComicCraft, an AI comic story creator.

Create a structured 5-panel comic outline.

Story Prompt: {story_prompt}
Main Character: {character_name}
Setting: {setting}
Tone: {tone}
Art Style: {art_style}

Return ONLY valid JSON.

Create exactly 5 panels.

Each panel must contain:
panel
title
scene_description
image_prompt
"""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    text = response.text.strip()

    if text.startswith("```"):
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

    return json.loads(text)