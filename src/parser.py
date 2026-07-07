import json
import re


def parse_ai_response(response_text):

    # Empty response handling
    if not response_text:
        return {
            "score": 0,
            "summary": "Empty AI response.",
            "code_quality": "",
            "time_complexity": "",
            "space_complexity": "",
            "execution_result": "",
            "bugs": [],
            "issues": [],
            "performance_issues": [],
            "optimization_suggestions": [],
            "optimized_code": "",
            "final_verdict": "No response generated."
        }

    try:
        response_text = re.sub(r"```json|```", "", response_text).strip()

        # Extract JSON block
        start = response_text.find("{")
        end = response_text.rfind("}") + 1

        if start == -1 or end == 0:
            raise ValueError("No JSON object found")

        clean_json = response_text[start:end]

        # Remove invalid control characters
        clean_json = re.sub(r"[\x00-\x1F\x7F]", "", clean_json)

        # Parse JSON safely
        parsed = json.loads(clean_json)

        # Ensure all required keys exist
        parsed.setdefault("score", 0)
        parsed.setdefault("summary", "")
        parsed.setdefault("code_quality", "")
        parsed.setdefault("time_complexity", "")
        parsed.setdefault("space_complexity", "")
        parsed.setdefault("execution_result", "")
        parsed.setdefault("bugs", [])
        parsed.setdefault("performance_issues", [])
        parsed.setdefault("optimization_suggestions", [])
        parsed.setdefault("optimized_code", "")
        parsed.setdefault("final_verdict", "")

        # Backward compatibility for old frontend
        parsed.setdefault("issues", parsed.get("bugs", []))

        return parsed

    except Exception as e:

        return {
            "score": 0,
            "summary": "Failed to parse AI response.",
            "code_quality": "",
            "time_complexity": "",
            "space_complexity": "",
            "execution_result": "",
            "bugs": [
                {
                    "line": 1,
                    "severity": "info",
                    "problem": "AI response was not in expected JSON format",
                    "impact": str(e),
                    "fix": response_text[:1200]
                }
            ],
            "issues": [
                {
                    "line": 1,
                    "severity": "info",
                    "problem": "AI response was not in expected JSON format",
                    "impact": str(e),
                    "fix": response_text[:1200]
                }
            ],
            "performance_issues": [],
            "optimization_suggestions": [],
            "optimized_code": "",
            "final_verdict": "Parsing failed."
        }