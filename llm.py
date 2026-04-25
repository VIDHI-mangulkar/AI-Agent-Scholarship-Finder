import requests

def call_llm(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            },
            timeout=60   # 🔥 prevents infinite loading
        )

        return response.json().get("response", "No response")

    except Exception as e:
        return f"LLM ERROR: {str(e)}"
