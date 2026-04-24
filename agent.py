from tools import search_scholarships
from llm import generate_response

def scholarship_agent(profile):

    query = f"""
    Find scholarships and fellowships for:
    Field: {profile['field']}
    Nationality: {profile['nationality']}
    Level: {profile['level']}
    """

    results = search_scholarships(query)

    # Clean noisy results
    results = [r for r in results if r.get("content") and len(r["content"]) > 50]

    context = ""
    for r in results:
        context += f"""
Title: {r['title']}
Content: {r['content']}
URL: {r['url']}
---
"""

    prompt = f"""
You are a world-class scholarship AI advisor.

TASK:
From the data below, select, rank, and explain best scholarships.

DATA:
{context}

STRICT OUTPUT FORMAT:

## 🏆 Ranked Scholarships

1. Scholarship Name
   - Why it matches:
   - Eligibility:
   - Deadline:
   - Benefit:

2. Scholarship Name
   - Why it matches:
   - Eligibility:
   - Deadline:
   - Benefit:

## 📌 Application Tips
- Write 4 strong application tips

## ⚡ Final Summary
Give a short conclusion (2-3 lines)

RULES:
- MUST rank scholarships
- MUST use bullets
- MUST be structured
- Focus on best global opportunities
"""

    response = generate_response(prompt)

    return response, results