def get_review_prompt(code: str, max_tokens: int = 4096, gpt_model: str = "gpt-4o") -> dict:
    prompt_text = f"""You are an elite senior software engineer performing a professional, human-like code review.

Review the code below and return a single valid JSON object — no markdown, no extra text, just JSON.

RULES:
- Only flag real issues; never invent problems if the code is correct
- Prefer minimal, readable fixes over complex rewrites
- Preserve the original style and logic wherever possible
- Write feedback like a senior engineer, not a linter

SCORE GUIDE:
90-100 → production-ready | 70-89 → minor improvements | 50-69 → moderate issues | 30-49 → major problems | 0-29 → broken

REQUIRED JSON:
{{
  "score": <integer 0-100>,
  "summary": "<2-3 sentence overview>",
  "code_quality": "<brief quality assessment>",
  "time_complexity": "<e.g. O(n²)>",
  "space_complexity": "<e.g. O(n)>",
  "bugs": [
    {{
      "line": <integer or null>,
      "severity": "low|medium|high|critical",
      "problem": "<clear description>",
      "impact": "<what could go wrong>",
      "fix": "<concise fix or corrected snippet>"
    }}
  ],
  "security_issues": [
    {{
      "line": <integer or null>,
      "severity": "low|medium|high|critical",
      "vulnerability": "<description>",
      "fix": "<how to address it>"
    }}
  ],
  "performance_issues": [
    {{
      "line": <integer or null>,
      "issue": "<description>",
      "why_it_is_bad": "<performance impact>",
      "optimization": "<suggested improvement>"
    }}
  ],
  "optimization_suggestions": ["<actionable suggestion>"],
  "optimized_code": "<improved version, or empty string if already optimal>",
  "final_verdict": "<honest 2-3 sentence conclusion>"
}}

FEEDBACK STYLE EXAMPLES:

Bad: "Use hashmap."
Good: "The nested loops create O(n²) complexity. A dictionary reduces repeated lookups to O(1) and scales significantly better on large inputs."

Bad: "Bad variable name."
Good: "The variable 'sum' shadows Python's built-in sum() function, which can cause subtle bugs and confusion in larger codebases."

CODE TO REVIEW:

{code}

JSON:"""

    return {
        "model": gpt_model,
        "max_tokens": max_tokens,
        "temperature": 0.1,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a world-class AI code reviewer. "
                    "Return ONLY valid JSON — no markdown, no preamble. "
                    "Be realistic, specific, and human-like."
                )
            },
            {
                "role": "user",
                "content": prompt_text
            }
        ],
    }

