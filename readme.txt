# AI-Powered Feedback System

This project is a two-view Streamlit application for collecting and analyzing customer feedback using Large Language Models (LLMs).

## Features

### User App
- Users can submit a rating and textual feedback
- The system generates an AI-powered response to the user
- Feedback is stored persistently

### Admin Dashboard
- Displays all submitted feedback
- Generates AI summaries and recommended actions for each review
- Visualizes rating distribution

## Tech Stack
- Python
- Streamlit
- OpenRouter (LLM API)
- Pandas

## How to Run Locally

1. Install dependencies:pip install -r requirements.txt

2. Set environment variable:OPENROUTER_API_KEY=<your_api_key>

3. Run apps:streamlit run user_app.py
	    streamlit run admin_app.py

## Notes
- API keys are not hardcoded and must be set as environment variables.
- The project is designed to be deployment-ready on Streamlit Cloud.


