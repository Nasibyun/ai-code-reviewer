# def get_review_prompt(code, max_tokens, gpt_model):

#     prompt_text = f"""
# You are an expert AI code reviewer.

# Analyze the following code and return ONLY valid JSON.

# IMPORTANT:
# - Keep explanations concise but meaningful
# - Detect real bugs only
# - Preserve original coding style
# - Avoid overengineering
# - Keep optimized code readable

# REQUIRED JSON FORMAT:

# {{
#   "score": 0,
#   "summary": "",
#   "time_complexity": "",
#   "space_complexity": "",

#   "bugs": [
#     {{
#       "line": 0,
#       "severity": "low|medium|high|critical",
#       "problem": "",
#       "fix": ""
#     }}
#   ],

#   "optimization_suggestions": [
#     ""
#   ],

#   "optimized_code": "",

#   "final_verdict": ""
# }}

# Review this code:

# {code}

# JSON:
# """

#     return {
#         "max_tokens": 1200,
#         "temperature": 0.1,
#         "messages": [
#             {
#                 "role": "system",
#                 "content": (
#                     "You are a professional AI code reviewer. "
#                     "Return ONLY valid JSON."
#                 )
#             },
#             {
#                 "role": "user",
#                 "content": prompt_text
#             }
#         ],
#     }


#  Currently cuz of api key limit cant cross the prompt limit otherwise will take lot more time

def get_review_prompt(code, max_tokens, gpt_model):

    prompt_text = f"""
You are an elite senior software engineer performing a PROFESSIONAL and HUMAN-LIKE code review.

Your task is to:
- detect bugs
- explain issues clearly
- analyze performance
- improve readability
- preserve the original coding style whenever possible
- avoid unnecessary overengineering

IMPORTANT RULES:

1. Return ONLY valid JSON
2. No markdown formatting
3. No explanations outside JSON
4. Keep explanations realistic and beginner-friendly
5. Prefer minimal fixes before advanced rewrites
6. Do NOT rewrite simple code into unnecessarily advanced code
7. Keep optimized_code readable and practical
8. Preserve original logic when possible
9. Avoid unnecessary libraries unless truly useful
10. If the code is already correct, do not invent fake problems

SCORING GUIDE:
- 90-100 → excellent / production ready
- 70-89 → good with small improvements needed
- 50-69 → moderate issues
- 30-49 → major problems
- 0-29 → broken or highly inefficient

REQUIRED JSON FORMAT:

{{
  "score": 0,

  "summary": "",

  "code_quality": "",

  "time_complexity": "",

  "space_complexity": "",

  "execution_result": "",

  "bugs": [
    {{
      "line": 0,
      "severity": "low|medium|high|critical",
      "problem": "",
      "impact": "",
      "fix": ""
    }}
  ],

  "performance_issues": [
    {{
      "line": 0,
      "issue": "",
      "why_it_is_bad": "",
      "optimization": ""
    }}
  ],

  "optimization_suggestions": [
    ""
  ],

  "optimized_code": "",

  "final_verdict": ""
}}

GOOD REVIEW STYLE EXAMPLES:

Bad:
"Use hashmap."

Good:
"The nested loops increase runtime to O(n²). 
Using a dictionary can reduce repeated lookups and improve performance on large datasets."

Bad:
"Bad variable name."

Good:
"The variable name 'sum' shadows Python's built-in sum() function, which can reduce readability and may lead to confusion later."

Review this code carefully:

{code}

JSON:
"""

    return {
        "max_tokens": 4096,
        "temperature": 0.1,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a world-class AI code reviewer. "
                    "Return ONLY valid JSON. "
                    "Be realistic, detailed, and human-like. "
                    "Preserve readability and avoid overengineering."
                )
            },
            {
                "role": "user",
                "content": prompt_text
            }
        ],
    }

