# 🤖 Multi-AI-Agent Job Hunt Assistant

> An AI-powered job application assistant built with CrewAI, Groq, and Streamlit that automates the entire job application process using multiple specialized AI agents.

## 🌐 Live Demo
👉 [Launch Fraud Detection App](https://productankur-multi-ai-agent-job-hunt-assistant.streamlit.app)

---

## 📌 What is this project?

Job hunting is time-consuming. Writing tailored cover letters, analyzing job descriptions, and crafting LinkedIn messages for every job posting takes hours.

This project automates that entire process using a **multi-agent AI system** — multiple specialized AI agents working together, each doing one specific job, to generate personalized application materials in minutes.

---

## 🎯 What does it do?

1. **Search real job listings** from the USAJobs API based on your keyword and location
2. **Analyze the job description** and extract key responsibilities, skills, and qualifications
3. **Generate a tailored resume summary and cover letter** matched to the job
4. **Draft a personalized LinkedIn outreach message** to the hiring manager

All of this happens automatically with a single click.

---

## 🧠 How does it work?

The system uses **3 specialized AI agents** orchestrated by CrewAI:

- **Agent 1: Job Description Analyst**
  - Reads the job posting
  - Extracts key requirements, skills, and qualifications

- **Agent 2: Resume and Cover Letter Writer**
  - Reads your resume and job analysis
  - Writes a tailored resume summary and cover letter

- **Agent 3: LinkedIn Outreach Specialist**
  - Reads job details and your background
  - Drafts a personalized LinkedIn message

Each agent's output feeds into the next — like an assembly line of AI workers.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| CrewAI | Multi-agent orchestration framework |
| Groq (LLaMA 3.3 70B) | LLM powering the AI agents |
| Streamlit | Web application interface |
| USAJobs API | Real-time federal job listings |
| LiteLLM | Universal LLM interface |
| GitHub | Version control |
| Streamlit Cloud | App deployment |

---

## 📁 Project Structure

Multi-AI-Agent-Job-Hunt-Assistant/
├── agents/
│   ├── jd_analyst.py          # Job Description Analyst agent
│   ├── resume_cl_agent.py     # Resume and Cover Letter agent
│   └── messaging_agent.py     # LinkedIn Messaging agent
├── data/
│   ├── sample_resume.txt      # Default resume input
│   └── cover_letters/         # Generated cover letters
├── utils/
│   ├── config.py              # API key configuration
│   ├── tracking.py            # Application logging
│   └── usajobs_api.py         # USAJobs API integration
├── streamlit_app.py           # Main Streamlit application
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation

---

## 🚀 How to Run Locally

### Prerequisites
- Python 3.11+
- Groq API key (free at [console.groq.com](https://console.groq.com))
- USAJobs API key (free at [developer.usajobs.gov](https://developer.usajobs.gov))

### Installation

```bash
# Clone the repository
git clone https://github.com/productankur/Multi-AI-Agent-Job-Hunt-Assistant.git

# Navigate to project folder
cd Multi-AI-Agent-Job-Hunt-Assistant

# Install dependencies
pip install -r requirements.txt
```

### Configure API Keys
Create a utils/.env file:

GROQ_API_KEY=your_groq_api_key
USAJOBS_API_KEY=your_usajobs_api_key

### Run the app
```bash
streamlit run streamlit_app.py
```

---

## 💡 Key Concepts Demonstrated

- **Multi-Agent Systems** — multiple AI agents collaborating on a shared goal
- **Prompt Engineering** — designing effective instructions for each agent
- **API Integration** — consuming REST APIs with authentication
- **Asynchronous Programming** — running agents without blocking the UI
- **Streamlit Development** — building interactive web apps in pure Python
- **Cloud Deployment** — deploying apps on Streamlit Cloud
- **Secret Management** — securing API keys in production

---

## 🔮 Future Improvements

- Add download button for generated materials
- Implement application history tracker
- Add email integration to send materials directly
- Support more job boards beyond USAJobs
- Add interview preparation agent
- Implement resume parsing from PDF upload

---

## 👨‍💻 About the Author

Built by **Ankur** — a Product Manager with a passion for AI and machine learning.

This project was built to demonstrate hands-on experience with:
- Agentic AI systems
- Python development
- Cloud deployment

Connect with me on LinkedIn (https://www.linkedin.com/in/ankurratwaya/)

---

## 📄 License
MIT License — feel free to use and modify this project.
