import os
import requests
import json
import re
from dotenv import load_dotenv

# Only working model using current api key
WORKING_MODELS = [
    "gemini-flash-lite-latest",
    "gemini-2.5-flash",
    "gemma-4-26b-a4b-it",
    "gemini-flash-latest",
    "gemini-2.5-flash-lite",
    "gemini-3.1-flash-lite-preview",
    "gemini-robotics-er-1.6-preview"
]

def send_request(api_key, payload, spinner_text):
    load_dotenv()
    
    if not api_key:
        api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        print("No API key found")
        return None
    
    print(spinner_text)
    
    # Try each working model until one succeeds
    for model in WORKING_MODELS:
        try:
            prompt_text = ""
            for msg in payload.get("messages", []):
                prompt_text += msg.get("content", "") + "\n"

            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
            
            print(f"Trying model: {model}")
            
            response = requests.post(
                url,
                params={"key": api_key},
                json={
                    "contents": [{"parts": [{"text": prompt_text}]}],
                    "generationConfig": {
                        "temperature": payload.get("temperature", 0.1),
                        "maxOutputTokens": payload.get("max_tokens", 2000),
                    }
                },
                timeout=10
            )
            
            if response.status_code == 200:
                result = response.json()
                if "candidates" in result and result["candidates"]:
                    content = result["candidates"][0]["content"]["parts"][0]["text"]
                    content = re.sub(r'```json\s*', '', content)
                    content = re.sub(r'```\s*', '', content)
                    content = re.sub(r'```python\s*', '', content)
                    print(f"✅ Model {model} worked!")
                    return content.strip()
            else:
                print(f"⚠️ Model {model} failed: {response.status_code}")
                continue
                
        except Exception as e:
            print(f"❌ Model {model} error: {str(e)[:50]}")
            continue
    
    # If all models fail
    return {
        "error": "All models failed. Please try again in a few minutes.",
        "tested_models": WORKING_MODELS
    }