import streamlit as st
import sys
import os
import asyncio
import uvloop
import importlib.util
import litellm
import time

litellm.cache = None

# Base path - works everywhere
base = os.path.dirname(os.path.abspath(__file__))
sys.path.append(base)
sys.path.append(os.path.join(base, "utils"))

# Secret keys - works on both Colab and Streamlit Cloud
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    USAJOBS_API_KEY = st.secrets["USAJOBS_API_KEY"]
    os.environ["GROQ_API_KEY"] = GROQ_API_KEY
    os.environ["USAJOBS_API_KEY"] = USAJOBS_API_KEY
except:
    from config import GROQ_API_KEY, USAJOBS_API_KEY

# Page config
st.set_page_config(
    page_title="Multi AI Agent - Job Hunt Assistant",
    page_icon="💼",
    layout="wide"
)

st.title("💼 AI Job Hunt Assistant")
st.markdown("*Powered by CrewAI + Groq*")

# Sidebar inputs
st.sidebar.header("🔍 Job Search")
keyword = st.sidebar.text_input("Job Keyword", value="data analyst")
location = st.sidebar.text_input("Location", value="remote")
results_per_page = st.sidebar.slider("Number of Results", 1, 10, 5)

# Resume input
st.sidebar.header("📄 Your Resume")
resume_path = os.path.join(base, "data", "sample_resume.txt")
with open(resume_path, "r") as f:
    default_resume = f.read()
resume = st.sidebar.text_area("Paste your resume here", value=default_resume, height=300)

# Fetch jobs button
if st.sidebar.button("🔎 Search Jobs"):
    with st.spinner("Fetching jobs from USAJobs..."):
        spec = importlib.util.spec_from_file_location("usajobs_api", os.path.join(base, "utils", "usajobs_api.py"))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        jobs = mod.fetch_usajobs(keyword, location, results_per_page)
        st.session_state["jobs"] = jobs
        st.success(f"✅ Found {len(jobs)} jobs!")

# Display jobs
if "jobs" in st.session_state:
    st.header("📋 Job Listings")
    jobs = st.session_state["jobs"]

    for i, job in enumerate(jobs):
        descriptor = job.get("MatchedObjectDescriptor", {})
        title = descriptor.get("PositionTitle", "N/A")
        agency = descriptor.get("OrganizationName", "N/A")
        loc = descriptor.get("PositionLocationDisplay", "N/A")
        url = descriptor.get("ApplyURI", [""])[0]
        summary = descriptor.get("UserArea", {}).get("Details", {}).get("JobSummary", "N/A")

        with st.expander(f"💼 {title} — {agency}"):
            st.write(f"📍 **Location:** {loc}")
            st.write(f"📝 **Summary:** {summary}")
            st.markdown(f"[🔗 Apply Here]({url})")

            if st.button(f"🤖 Generate Application Materials", key=f"apply_{i}"):
                st.session_state["selected_job"] = descriptor

# Generate application materials
if "selected_job" in st.session_state:
    descriptor = st.session_state["selected_job"]
    job_title = descriptor.get("PositionTitle", "")
    agency = descriptor.get("OrganizationName", "")
    job_description = descriptor.get("UserArea", {}).get("Details", {}).get("JobSummary", "")

    st.header("🤖 Generating Application Materials...")

    # Load agents
    spec1 = importlib.util.spec_from_file_location("jd_analyst", os.path.join(base, "agents", "jd_analyst.py"))
    jd_analyst = importlib.util.module_from_spec(spec1)
    spec1.loader.exec_module(jd_analyst)

    spec2 = importlib.util.spec_from_file_location("resume_cl_agent", os.path.join(base, "agents", "resume_cl_agent.py"))
    resume_cl = importlib.util.module_from_spec(spec2)
    spec2.loader.exec_module(resume_cl)

    spec3 = importlib.util.spec_from_file_location("messaging_agent", os.path.join(base, "agents", "messaging_agent.py"))
    messaging = importlib.util.module_from_spec(spec3)
    spec3.loader.exec_module(messaging)

    def run_all_agents():
        loop = uvloop.new_event_loop()
        asyncio.set_event_loop(loop)

        async def _run():
            from crewai import Crew

            # Agent 1
            agent1 = jd_analyst.get_jd_analyst_agent()
            task1 = jd_analyst.create_jd_analysis_task(agent1, job_description)
            crew1 = Crew(agents=[agent1], tasks=[task1], verbose=True)
            result1 = await crew1.kickoff_async()
            time.sleep(10)  # Wait 10 seconds before next agent

            # Agent 2
            agent2 = resume_cl.get_resume_cl_agent()
            task2 = resume_cl.create_resume_cl_task(agent2, job_description, resume)
            crew2 = Crew(agents=[agent2], tasks=[task2], verbose=True)
            result2 = await crew2.kickoff_async()
            time.sleep(10)  # Wait 10 seconds before next agent

            # Agent 3
            agent3 = messaging.get_messaging_agent()
            task3 = messaging.create_messaging_task(agent3, job_title, agency, resume[:500])
            crew3 = Crew(agents=[agent3], tasks=[task3], verbose=True)
            result3 = await crew3.kickoff_async()

            return f"{result1}\n\n---\n\n{result2}\n\n---\n\n{result3}"

        return loop.run_until_complete(_run())

    with st.spinner("⏳ AI agents are working... (this may take up to 1 minute)"):
        result = run_all_agents()

    st.success("✅ Application materials generated!")
    st.markdown(result)
