from crewai import Agent, Task, LLM
import sys
import os
import litellm

litellm.cache = None

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from config import GROQ_API_KEY

os.environ["GROQ_API_KEY"] = GROQ_API_KEY

llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY
)

def get_jd_analyst_agent():
    return Agent(
        role="Job Description Analyst",
        goal="Analyze job descriptions and extract key requirements, skills, and responsibilities",
        backstory="You are an expert career coach with years of experience analyzing job postings and identifying what employers really want.",
        llm=llm,
        verbose=True
    )

def create_jd_analysis_task(agent, job_description, PositionTitle, OrganizationName):
    return Task(
        description=f"""Analyze the following job description and extract key details:

        Job Description: {job_description}

        Job Title: {PositionTitle}

        Agency: {OrganizationName}

        Extract and organize:
        1. Job Title and Agency
        2. Key Responsibilities
        3. Required Skills
        4. Qualifications
        5. Salary and Location
        """,
        expected_output="""A structured markdown report with sections for:
        - Job Overview
        - Key Responsibilities
        - Required Skills
        - Qualifications
        - Salary and Location
        """,
        agent=agent,
        output_file="/drive/MyDrive/job_hunt_assistant/data/report.md"
    )
