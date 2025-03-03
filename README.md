# PM-Agent
A team of Agents to help Product Manager analyse the competition and provide recommendations

## Tech Stack used
1. API : Groq API
2. UI : Streamlit
3. Agents:Crew.ai
4. LLM : llm_llama70b

## Agents
  1. Competitor Analyst Agent
  2. Feature Comparison Specialist Agent
  3. Strategic Advisor Agent

## Notes:
1. Streamlitapp.py : Uses streamlit for UI
2. app.py : Runs on the local terminal without UI
3. requirements.txt : Required libraries
4. config.py : Configure Groq API
5. Create .env file and assign Groq API key to varibale GROQ_API_KEY

## Acceess App Here:
https://huggingface.co/spaces/Jayateerth/PM-Agent

## Screenshot of App

<img width="1364" alt="Screenshot 2025-02-19 at 3 51 09 PM" src="https://github.com/user-attachments/assets/f2e6a2a5-a164-47f7-abf6-89f3474da322" />

## Documentation
Overview:
The application generates a comprehensive competitor analysis and strategic recommendations report for a product. The process is broken down into several stages, each handled by a specialized agent.

Steps:

User Input:

The user enters a product name into the UI (via Streamlit).
Crew AI Workflow Initiation:

Once the "Generate Report" button is clicked, the app initializes the workflow.
The input (product name) is passed to the Crew AI system.
Agent Tasks Execution:
The workflow is composed of several tasks managed by different agents:

1. Competitor Analyst Agent:
Goal: Identify the main competitors for the product.
Task: Produce a competitor analysis document, including a SWOT analysis for each competitor.

2. Feature Comparison Specialist Agent:
Goal: Compare the product's features against its competitors.
Task: Generate a detailed feature comparison report, highlighting strengths, weaknesses, and opportunities.

3. Strategic Advisor Agent:
Goal: Provide strategic recommendations based on the analysis.
Task: Synthesize insights from the previous tasks and generate actionable recommendations along with a roadmap and resource guidance.
Final Report Generation:

The outputs from the agents are combined to form a final report.

This report is displayed in the UI and also converted into a downloadable PDF.

User Output:

The final report is shown on the Streamlit app.
A download button allows the user to save the report as a PDF with a dynamic filename.
