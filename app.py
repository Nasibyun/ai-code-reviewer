from fastapi import FastAPI
from pydantic import BaseModel
import os
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from src.reviewer import review_code_logic
from src.fixer import fix_code
from src.executor import run_code
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.mount("/static", StaticFiles(directory="./"), name="static")

class CodeInput(BaseModel):
    code: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve UI
@app.get("/", response_class=HTMLResponse)
def serve_ui():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/review")
def review_code(data: CodeInput):
    try:
        result = review_code_logic(data.code)
        return result
    except Exception as e:
        return {
            "score": 0,
            "summary": "The AI is currently unavailable.",
            "issues": [
                {
                    "type": "error",
                    "title": "API Error",
                    "problem": str(e),
                    "line": 0,
                    "fix": "Please check your API configuration."
                }
            ]
        }

@app.post("/fix")
def fix(data: CodeInput):
    try:
        fixed = fix_code(data.code)
        return {"fixed_code": fixed}
    except Exception as e:
        return {"error": str(e)}

@app.post("/run")
def execute(data: CodeInput):
    try:
        return run_code(data.code)
    except Exception as e:
        return {"error": str(e)}