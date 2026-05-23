from crewai import Agent, Task, LLM
import sys
import os
import litellm

litellm.cache = None

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))

try:
    import streamlit as st
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except:
    from config import GROQ_API_KEY

os.environ["GROQ_API_KEY"] = GROQ_API_KEY

llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY
)

def get_messaging_agent():
    return Agent(
        role="LinkedIn Outreach Specialist",
        goal="Draft personalized and compelling LinkedIn outreach messages to hiring managers",
        backstory="You are an expert in professional networking with years of experience crafting personalized outreach messages that get responses. You know how to strike the perfect balance between professional and personable.",
        llm=llm,
        verbose=True
    )

def create_messaging_task(agent, job_title, agency, resume_summary):
    return Task(
        description=f"""Draft a personalized LinkedIn outreach message for the following:

        Job Title: {job_title}
        Agency: {agency}
        Candidate Summary: {resume_summary}

        The message should:
        - Be concise (under 300 words)
        - Be professional yet personable
        - Mention the specific job and agency
        - Highlight 1-2 key strengths from the candidate summary
        - End with a clear call to action
        """,
        expected_output="""A short, personalized LinkedIn outreach message ready to send.""",
        agent=agent,
        output_file="data/linkedin_message.txt"
    )
