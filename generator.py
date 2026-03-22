import subprocess

def simplify(text, meanings):
    prompt = f"""
Simplify this Hindi sentence:

Sentence: {text}

Replace difficult words using:
{meanings}

Output:
- simplified sentence
- meanings
"""

    try:
        result = subprocess.run(
            ["ollama", "run", "llama3"],
            input=prompt.encode("utf-8"),   # ✅ Fix for Unicode
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        output = result.stdout.decode("utf-8")
        return output

    except Exception as e:
        return f"Error: {str(e)}"