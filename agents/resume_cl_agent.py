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

def get_resume_cl_agent():
    return Agent(
        role="Resume and Cover Letter Writer",
        goal="Tailor resumes and write compelling cover letters based on job descriptions",
        backstory="You are an expert career consultant with years of experience helping candidates land their dream jobs by crafting personalized resumes and cover letters that match job requirements perfectly.",
        llm=llm,
        verbose=True
    )

def create_resume_cl_task(agent, job_description, resume):
    return Task(
        description=f"""Based on the following job description and candidate resume, create:
        1. A tailored resume summary (3-4 sentences)
        2. A compelling cover letter

        Job Description:
        {job_description}

        Candidate Resume:
        {resume}

        Make sure to:
        - Highlight relevant skills and experience
        - Match keywords from the job description
        - Keep the cover letter professional and concise
        """,
        expected_output="""A markdown document containing:
        - Tailored Resume Summary
        - Full Cover Letter
        """,
        agent=agent,
        output_file="data/cover_letters/cover_letter.md"
    )
