from llm import generate_response

def evaluate_output(output):

    prompt = f"""
You are a STRICT but FAIR academic evaluator.

Evaluate this scholarship AI output:

{output}

Use scoring:

1. Relevance (0-10)
2. Completeness (0-10)
3. Structure (0-10)

IMPORTANT RULES:
- Be slightly generous for good structured answers
- Do NOT penalize minor formatting issues
- Reward ranking quality and clarity

Return ONLY:

Relevance: X/10
Completeness: X/10
Structure: X/10
Final Score: X/10
"""

    return generate_response(prompt)
