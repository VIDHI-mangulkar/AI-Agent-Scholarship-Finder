import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_model():
    models = genai.list_models()

    for m in models:
        if "generateContent" in m.supported_generation_methods:
            return m.name

    return "models/gemini-pro"

model = genai.GenerativeModel(get_model())

def generate_response(prompt):
    response = model.generate_content(prompt)
    return response.text