import os
from tavily import TavilyClient

# works in both local + streamlit cloud
api_key = os.getenv("TAVILY_API_KEY")

client = TavilyClient(api_key=api_key)

def search_scholarships(query):

    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=8
    )

    return response["results"]
