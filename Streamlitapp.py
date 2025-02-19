# Import necessary packages
import os
import statsapi
import datetime
from datetime import date, timedelta, datetime
import pandas as pd
import numpy as np
from crewai_tools import tool
from crewai import Agent, Task, Crew, Process
from langchain_groq import ChatGroq
from getpass import getpass
from fpdf import FPDF
import streamlit as st
from config import GROQ_API_KEY


# Set the page title and layout
st.title("Product Manager Competitor Analysis")
st.write("Enter a product name to generate a competitor analysis and strategic recommendations.")

# Sidebar content
st.sidebar.title("By: Jayateerth Katti")
st.sidebar.markdown("[LinkedIn Profile](https://www.linkedin.com/in/jayateerth-katti-10103a14/)")

# Get user input for product name
product = st.text_input("Product Name", "XYZ Software Testing Tool")

if st.button("Generate Report"):
    
    if not product:
        
        st.error("Please enter a product name.")
    
    else:

        st.info("Generating report. Please wait...")

        # Initialize LLM models
        llm_llama70b = ChatGroq(model_name="llama3-70b-8192")
        llm_llama8b = ChatGroq(model_name="llama3-8b-8192")
        llm_gemma2   = ChatGroq(model_name="gemma2-9b-it")
        llm_mixtral  = ChatGroq(model_name="mixtral-8x7b-32768")

        # Define agents
        # 1. Competitor Analyst Agent: Gathers competitor information and SWOT analysis.
        competitor_analyst = Agent(
            llm=llm_llama70b,
            role="Competitor Analyst",
            goal="Conduct an in-depth competitor analysis for {product}",
            backstory=(
                "You are a market analyst specializing in competitor analysis. Your task is to identify and analyze "
                "the key competitors for {product}. Gather data on each competitor’s features, pricing, market positioning, "
                "and perform a SWOT analysis (Strengths, Weaknesses, Opportunities, Threats). Your analysis should help a "
                "product manager understand the competitive landscape."
            ),
            allow_delegation=False,
            verbose=True,
            max_rpm=10
        )
        # 2. Feature Comparison Specialist: Compares product features against competitors.
        feature_comparison = Agent(
            llm=llm_llama70b,
            role="Feature Comparison Specialist",
            goal="Compare and contrast the features of {product} with its key competitors",
            backstory=(
                "Your role is to analyze and compare the features of {product} against its competitors. Identify areas "
                "where {product} excels, falls short, or matches the competition. Highlight any innovative features or gaps "
                "that could represent opportunities for improvement."
            ),
            allow_delegation=False,
            verbose=True
        )
        # 3. Strategic Advisor: Synthesizes insights to recommend strategic actions.
        strategic_advisor = Agent(
            llm=llm_llama70b,
            role="Strategic Advisor",
            goal="Provide strategic recommendations for {product} based on competitor analysis and feature comparison",
            backstory=(
                "You are a seasoned product strategist. Based on the competitor analysis and feature comparison, "
                "synthesize key insights and propose actionable recommendations. Your recommendations should help the product "
                "improve its market position, address feature gaps, and capitalize on identified opportunities."
            ),
            allow_delegation=False,
            verbose=True
        )
        #Define Tasks
        # Task 1: Competitor Analysis
        competitor_analysis_task = Task(
            description=(
                "1. Identify the main competitors for {product}.\n"
                "2. For each competitor, list their key features, pricing strategy, market positioning, "
                "and unique selling propositions.\n"
                "3. Perform a SWOT analysis for each competitor."
            ),
            expected_output=(
                "A detailed competitor analysis document that outlines the main competitors for {product} along with a SWOT analysis for each."
            ),
            agent=competitor_analyst,
        )

        # Task 2: Feature Comparison
        feature_comparison_task = Task(
            description=(
                "1. Based on the competitor analysis, compare the features of {product} with those of its competitors.\n"
                "2. Highlight areas where {product} outperforms, matches, or lags behind the competition.\n"
                "3. Identify any unique features or gaps that could be leveraged for competitive advantage.\n"
                "4. Be sure to integrate and highlight the key findings from the feature comparison report—such as areas where {product} excels or lags behind its competitors—and offer actionable advice to improve the product's competitive position."
            ),
            expected_output=(
                "A comprehensive feature comparison report that clearly illustrates how {product} stacks up against its competitors."
            ),
            agent=feature_comparison,
        )

        # Task 3: Strategic Recommendations
        strategic_recommendations_task = Task(
            description=(
                "Review the competitor analysis and feature comparison reports. Based on the insights, propose strategic recommendations for {product}.\n"
                "Focus on actionable strategies to improve competitive positioning, enhance feature offerings, and address market gaps."
            ),
            expected_output=(
                "Name of the product user provided.List of competitors analysed.Detailed Feature Comparison Report.And a set of actionable strategic recommendations for {product} that provides clear guidance on improving its competitive stance."
            ),
            agent=strategic_advisor,
            #human_input=True  # Allows for human adjustments if needed
        )
        #crwate Crew
        crew = Crew(
            agents=[competitor_analyst, feature_comparison, strategic_advisor],
            tasks=[competitor_analysis_task, feature_comparison_task, strategic_recommendations_task],
            verbose=2
        )

        #Kick-off crew AI
        result = crew.kickoff(inputs={"product": product})

    # Convert result to string (assuming it's text) and print the final report
        final_report = str(result)
        st.markdown("### Final Report")
        st.markdown(final_report)
    