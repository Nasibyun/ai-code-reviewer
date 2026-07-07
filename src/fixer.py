import os
from dotenv import load_dotenv
import requests
import re

# Only working models in gemini atp for me 
WORKING_MODELS = [
    "gemini-flash-lite-latest",
    "gemini-2.5-flash",
    "gemma-4-26b-a4b-it",
    "gemini-flash-latest",
    "gemini-2.5-flash-lite",
    "gemini-3.1-flash-lite-preview",
    "gemini-robotics-er-1.6-preview"
]

def fix_code(code):
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY") 
    if not api_key:
        return "Error: API key not set."

    prompt_text = f"""Fix this code and return ONLY the corrected code.
Do NOT include any explanations, just the fixed code.
Keep the same functionality, just fix bugs/errors.

Code to fix:
{code}
"""
    
    # Try each working model
    for model in WORKING_MODELS:
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
            
            response = requests.post(
                url,
                params={"key": api_key},
                json={
                    "contents": [{"parts": [{"text": prompt_text}]}],
                    "generationConfig": {
                        "temperature": 0.1,
                        "maxOutputTokens": 2000,
                    }
                },
                timeout=30
            )
            if response.status_code == 200:
                result = response.json()
                if "candidates" in result and result["candidates"]:
                    content = result["candidates"][0]["content"]["parts"][0]["text"]
                    content = re.sub(r'```python\s*', '', content)
                    content = re.sub(r'```\s*', '', content)
                    print(f"✅ Fixer used model: {model}")
                    return content.strip()
                    
        except Exception as e:
            continue
    
    return "Error: No working models available. Please try again."