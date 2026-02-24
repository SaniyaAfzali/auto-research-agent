                                                        **🔎 AutoResearch Agent  **
                               ** Autonomous Multi-Step AI Research System using LangGraph + Groq + Streamlit**
**Live Demo**

Deployed App:
👉 https://auto-research-agent-bqvkebxds9ubjbj6clymu7.streamlit.app/


**Project Overview**

The AutoResearch Agent is an autonomous AI system that performs structured, multi-step research on user queries.
Unlike a simple chatbot, this agent:

Breaks complex questions into sub-tasks

Uses external tools (search) intelligently

Evaluates its own output

Iterates when necessary

Synthesizes information into a final structured answer

Outputs a confidence score

The system is built using LangGraph orchestration with a reasoning loop (Planner → Researcher → Critic → Synthesizer).

**⚙️ Tech Stack**

Orchestration: LangGraph

LLM Provider: Groq (LLaMA 3.3 70B)

UI: Streamlit

Language: Python 3.10+

Version Control: Git + GitHub

**🔄 Multi-Step Reasoning Pattern**

The agent follows a Plan-and-Execute + Self-Critique loop:

1️⃣ Planner

Breaks main query into sub-questions.

2️⃣ Researcher

Generates research content.

Uses LLM (and optional search tool).

3️⃣ Critic

Evaluates:

Completeness

Logical consistency

Missing information

If incomplete → loops back to Researcher.

4️⃣ Synthesizer

Produces:

Final structured answer

Confidence score (0–1)


**🏗️ System Architecture**

<img width="344" height="722" alt="image" src="https://github.com/user-attachments/assets/91e10943-775a-4762-b5e3-29404d85788e" />



**⚙️ Installation & Setup**

1️⃣ Clone Repository

git clone https://github.com/SaniyaAfzali/auto-research-agent.git

cd auto-research-agent

2️⃣ Create Virtual Environment

python -m venv venv

venv\Scripts\activate   # Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Set Environment Variables

Create a .env file:

GROQ_API_KEY=your_key_here

TAVILY_API_KEY=your_key_here

5️⃣ Run Application
streamlit run app.py

**📌 Submission Components Included**

✔ Full Source Code

✔ LangGraph-based Orchestration

✔ Thinking Log Visualization

✔ Confidence Score

✔ README with Architecture

✔ Deployment Ready (Streamlit)

**🚀 Future Improvements**

Add citation linking in UI

Add memory between sessions

Add PDF export of research reports

Add cost/token tracking dashboard

**👩‍💻 Author**

Saniya Afzali
