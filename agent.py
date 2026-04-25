from tools import search_scholarships
from llm import call_llm


# 1. Build query
def build_query(profile):
    return f"""
Find scholarships for:
Field: {profile['field']}
Nationality: {profile['nationality']}
Academic Level: {profile['level']}
"""


# 2. Extract scholarships
def extract_scholarships(results):
    prompt = f"""
Extract scholarships from this data:

{results}

Return structured JSON:
- name
- eligibility
- deadline
- benefits
- link
"""
    return call_llm(prompt)


# 3. Rank scholarships
def rank_scholarships(data):
    prompt = f"""
Rank these scholarships based on:
- relevance
- ease of eligibility
- benefits

Data:
{data}

Return ranked list with reasoning.
"""
    return call_llm(prompt)


# 4. Generate tips
def generate_tips(ranked):
    prompt = f"""
Give application tips:

{ranked}

Include:
- strategy
- mistakes to avoid
- success tips
"""
    return call_llm(prompt)


# 🔥 FULL PIPELINE
def run_agent(profile):
    query = build_query(profile)

    search_results = search_scholarships(query)

    extracted = extract_scholarships(search_results)

    ranked = rank_scholarships(extracted)

    tips = generate_tips(ranked)

    return {
        "query": query,
        "search_results": search_results,
        "extracted": extracted,
        "ranked": ranked,
        "tips": tips
    }
