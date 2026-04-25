import streamlit as st
from agent import run_agent

st.set_page_config(page_title="AI Scholarship Agent", layout="centered")

st.title("🎓 AI Scholarship & Fellowship Agent (Ollama + LLaMA3)")

st.write("Enter student profile to find ranked scholarships")

# Input fields
field = st.text_input("Field of Study", value="MBA")
nationality = st.text_input("Nationality", value="India")
level = st.selectbox("Academic Level", ["Undergraduate", "Postgraduate", "PhD"])

# Button
if st.button("🔍 Find Scholarships"):
    try:
        # Show loading
        with st.spinner("Running AI agent... please wait ⏳"):
            
            profile = {
                "field": field,
                "nationality": nationality,
                "level": level
            }

            # Run agent
            result = run_agent(profile)

        st.success("Done!")

        # OUTPUT SECTIONS
        st.subheader("🔎 Search Query")
        st.write(result.get("query", "No query generated"))

        st.subheader("🌐 Search Results")
        st.json(result.get("search_results", {}))

        st.subheader("📌 Extracted Scholarships")
        st.text(result.get("extracted", "No extracted data"))

        st.subheader("🏆 Ranked Scholarships")
        st.text(result.get("ranked", "No ranking data"))

        st.subheader("💡 Application Tips")
        st.text(result.get("tips", "No tips generated"))

    except Exception as e:
        st.error("❌ Something went wrong")
        st.exception(e)
