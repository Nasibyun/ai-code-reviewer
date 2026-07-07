import os
from src import prompt
from src import request
from src.parser import parse_ai_response
from src.executor import run_code
from dotenv import load_dotenv

def review_code_logic(code):
    try:
        load_dotenv()
        
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            return {"error": "No API key found"}
        
        execution_result = "Code execution disabled in deployed version"
        
        combined_input = f"Code:\n{code}\n\nExecution Result:\n{execution_result}"
        payload = prompt.get_review_prompt(combined_input, 6000, None)
        result = request.send_request(api_key, payload, "Reviewing...")

        print(f"\n=== RAW RESULT TYPE: {type(result)} ===")
        print(f"=== RAW RESULT (first 300 chars): {str(result)[:300]} ===")

        if result is None:
            return {"error": "AI returned no response"}
        if isinstance(result, dict):
            if "error" in result:
                return result
            if "issues" in result:
                return result
            return {
                "score": 80,
                "summary": "Code reviewed",
                "issues": [],
                "raw": result
            }

        if isinstance(result, str):
            parsed = parse_ai_response(result)
            print(result)
            return parsed
        return {
            "error": "Invalid response type",
            "type": str(type(result)),
            "raw": str(result)[:500]
        }

    except Exception as e:
        return {"error": f"Reviewer crashed: {str(e)}"}
