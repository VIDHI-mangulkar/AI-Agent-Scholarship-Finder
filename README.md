# AI-Agent-Scholarship-Finder
                      AGENTIC AI REPORT
                   TOPIC: Scholarship Finder 
Group Members:
Role A (Architect and Integrator) - [Vidhi Mangulkar] [roll no-23]
Role B (Builder and Deployer) - [Gayatri Naidu] [roll no-15]

Git Hub: https://github.com/Gayatri-Naidu612/Scholarship-Finder-Agentic-AI.git
https://github.com/VIDHI-mangulkar/AI-Agent-Scholarship-Finder.git

Live Demo:

Date:23/4/2026
Semester IV[Btech ECE A]
 

PHASE 1 : PROBLEM STATEMENT 

PROBLEM:Given a student profile (field of study, nationality, academic level), agents search for applicable scholarships and fellowships via Tavily, summarize eligibility criteria and deadlines, and draft a prioritized list with application tips. The judge rates the relevance and completeness of the results.

Agent Solution : Student fills out a profile → Finder agent searches Tavily for scholarships → Eligibility Checker filters by criteria and deadline → Summary Agent ranks and drafts application tips. A Judge scores the output for relevance and completeness. 

USER PROBLEM :

Students spend hours on Google finding scholarships, most of which they are ineligible for
Deadlines are scattered across dozens of websites — easy to miss
No single tool filters by nationality, field, and academic level together
Students don't know how to prioritise or what to write — no tailored tips


Why Simple Chatbot Fails:
No live web access — scholarship data is outdated or hallucinated
Can't loop and verify eligibility for each result against a real student profile
Single prompt can't handle search + filter + summarise + evaluate in one go
No quality check — output may be irrelevant with no way to know

USER PERSONA :
Name: Priya Sharma 
Age: 20 
Degree: B.E. Computer Science, Pune
GPA: 8.4 / 10 
Nationality: Indian 
Goal: M.S. abroad (Germany / Canada)

Implementation (5 Key Points)
1.  Local LLM Integration using Ollama (LLaMA3)
The system uses Ollama with LLaMA3 model to perform all natural language processing tasks locally. This removes dependency on paid APIs, ensures privacy, and enables offline execution of the AI agent pipeline.

2.  Web Search Integration using Tavily API
The agent integrates Tavily Search API to fetch real-time scholarship and fellowship data from the web. This allows the system to retrieve updated opportunities based on user profile inputs like field, nationality, and academic level.

3.  Multi-Step Agent Pipeline Design
The system is designed as a sequential AI pipeline:
Query generation
Web search execution
Scholarship extraction
Ranking based on relevance
Application tips generation
Each step is handled modularly using separate functions for better scalability.

4 LLM-Based Evaluation (LLM-as-Judge)
A separate judge module evaluates the final output using LLaMA3. It scores results based on relevance, completeness, clarity, ranking quality, and usefulness. This introduces a self-evaluation mechanism similar to real-world AI systems.

5. Interactive Web Interface using Streamlit
The entire system is deployed as a Streamlit web application, allowing users to input their profile and instantly receive scholarship recommendations, rankings, and application guidance in a simple UI.
Pain: overwhelmed by options, unsure what she qualifies for, no guidance on applications
Needs: ranked shortlist + deadlines + specific tips she can act on immediately

voom viedo : 
app link : 


