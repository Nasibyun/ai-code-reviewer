import subprocess
import tempfile
import re
import os

def detect_language(code):
    code_lower = code.lower()

    # Python
    if "def " in code or "print(" in code:
        return "python"

    # C++
    if "#include" in code and "cout" in code:
        return "cpp"

    # JavaScript
    if "console.log" in code or "function " in code:
        return "javascript"

    # Java
    if "public class" in code:
        return "java"

    return "unknown"

def run_code(code):
    try:

        restricted = [
            "import os",
            "subprocess",
            "eval(",
            "exec(",
            "__import__",
        ]
        for keyword in restricted:
            if keyword.lower() in code.lower():
                return {
                    "output": "",
                    "error": f"Restricted keyword detected: {keyword}",
                    "language": "unknown"
                }
        # Detect lng
        language = detect_language(code)

        # Python
        if language == "python":

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".py",
                mode="w",
                encoding="utf-8"
            ) as f:
                f.write(code)
                file_name = f.name

            result = subprocess.run(
                ["python", file_name],
                capture_output=True,
                text=True,
                timeout=5
            )
            return {
                "output": result.stdout if result.stdout else "(no output)",
                "error": result.stderr if result.stderr else None,
                "language": language
            }

        # cpp
        elif language == "cpp":

            try:
                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".cpp",
                    mode="w",
                    encoding="utf-8"
                ) as f:
                    f.write(code)
                    cpp_file = f.name

                exe_file = cpp_file + ".exe"

                compile_result = subprocess.run(
                    ["g++", cpp_file, "-o", exe_file],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                if compile_result.returncode != 0:
                    return {
                        "output": "",
                        "error": compile_result.stderr,
                        "language": language
                    }
                run_result = subprocess.run(
                    [exe_file],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                return {
                    "output": run_result.stdout,
                    "error": run_result.stderr,
                    "language": language
                }

            except FileNotFoundError:
                return {
                    "output": "",
                    "error": "g++ compiler not installed.",
                    "language": language
                }

        # Javascript
        elif language == "javascript":
            try:
                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".js",
                    mode="w",
                    encoding="utf-8"
                ) as f:
                    f.write(code)
                    js_file = f.name

                result = subprocess.run(
                    ["node", js_file],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                return {
                    "output": result.stdout,
                    "error": result.stderr,
                    "language": language
                }

            except FileNotFoundError:
                return {
                    "output": "",
                    "error": "Node.js not installed.",
                    "language": language
                }

        # other language `will add later`
        else:
            return {
                "output": "",
                "error": f"{language.upper()} execution not supported locally.",
                "language": language
            }

    except subprocess.TimeoutExpired:
        return {
            "output": "",
            "error": "Execution timed out",
            "language": language if 'language' in locals() else "unknown"
        }

    except Exception as e:
        return {
            "output": "",
            "error": str(e),
            "language": language if 'language' in locals() else "unknown"
        }
