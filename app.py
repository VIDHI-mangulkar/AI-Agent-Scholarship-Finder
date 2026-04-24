import streamlit as st
from agent import scholarship_agent
from judge import evaluate_output

st.set_page_config(page_title="Scholarship AI Agent", layout="centered")

st.title("🎓 AI Scholarship & Fellowship Agent")

st.markdown("Enter student profile to get ranked scholarships with AI evaluation")

field = st.text_input("Field of Study")
nationality = st.text_input("Nationality")
level = st.selectbox("Academic Level", ["Undergraduate", "Postgraduate", "PhD"])

if st.button("Find Scholarships"):

    if not field or not nationality:
        st.error("Please fill all fields")
    else:
        profile = {
            "field": field,
            "nationality": nationality,
            "level": level
        }

        with st.spinner("AI Agent is analyzing scholarships..."):
            result, sources = scholarship_agent(profile)

        st.subheader("🏆 Ranked Scholarships")
        st.markdown(result)

        st.subheader("📊 AI Judge Score")
        score = evaluate_output(result)
        st.markdown(score)

        st.subheader("🔗 Sources")
        for s in sources:
            st.markdown(f"- [{s['title']}]({s['url']})")