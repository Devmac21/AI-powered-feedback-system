# AI-Powered Feedback System - Final Submission

## Project Overview
This is a comprehensive AI-powered feedback collection and analysis system built with Streamlit and OpenRouter LLM APIs. The system provides a dual-interface platform where customers can submit feedback and admins can analyze and act upon it.

## Architecture

### Core Components

1. **User Application** (`user_app.py`)
   - Rating slider (1-5 scale)
   - Text area for customer feedback
   - Real-time AI-generated responses using LLM
   - Automatic timestamp tracking with UTC timezone
   - Persistent storage of all submissions

2. **Admin Dashboard** (`admin_app.py`)
   - Comprehensive view of all customer feedback
   - AI-powered summaries for each review
   - Recommended action generation for business decisions
   - Visual analytics with rating distribution charts
   - Wide layout for better data exploration

3. **Utilities Module** (`utils.py`)
   - OpenRouter API integration for LLM calls
   - CSV-based data persistence
   - DataFrame operations for data management
   - Configuration management

4. **Prompts Engine** (`prompts.py`)
   - User-facing response prompt: empathetic and professional customer support responses
   - Admin-facing analysis prompt: concise summaries and actionable recommendations

## Key Features

✅ **AI-Powered Responses**: Uses Mistral 7B model via OpenRouter API
✅ **Persistent Storage**: CSV-based data store with automatic initialization
✅ **Dual Interfaces**: Separate user and admin applications
✅ **Real-time Analytics**: Visual rating distribution with Streamlit charts
✅ **UTC Timestamps**: All entries tracked with ISO format timestamps
✅ **Scalable Design**: Ready for Streamlit Cloud deployment
✅ **API Security**: Environment-based API key management (no hardcoding)

## Technology Stack

- **Frontend**: Streamlit (user-friendly web interface)
- **Backend**: Python
- **LLM Provider**: OpenRouter (mistralai/mistral-7b-instruct)
- **Data Storage**: Pandas + CSV
- **API Communication**: Requests library

## Setup & Installation

### Prerequisites
- Python 3.8+
- OpenRouter API key (obtain from https://openrouter.ai)

### Installation Steps

```bash
# 1. Clone the repository
git clone <repository_url>
cd fynd-task

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set environment variable (Windows PowerShell)
$env:OPENROUTER_API_KEY = "<your_api_key>"

# Or on Windows CMD
set OPENROUTER_API_KEY=<your_api_key>

# Or on Linux/Mac
export OPENROUTER_API_KEY=<your_api_key>
```

## Running the Application

### User Application
```bash
streamlit run user_app.py
```
- Opens on `http://localhost:8501` by default
- Submit feedback and receive AI responses

### Admin Dashboard
```bash
streamlit run admin_app.py
```
- Opens on `http://localhost:8502`
- View all submissions with AI-generated summaries and analytics

## Data Schema

Feedback entries are stored with the following structure:
```
timestamp (ISO format UTC)
rating (1-5)
review (customer feedback text)
ai_response (LLM-generated response to user)
summary (AI-generated summary for admin)
recommended_action (suggested business action)
```

## Configuration

Key configuration in `utils.py`:
- **Model**: `mistralai/mistral-7b-instruct` (can be changed)
- **Temperature**: 0.5 (for consistent, focused responses)
- **Max Tokens**: 250 (adequate for feedback responses)
- **API Endpoint**: `https://openrouter.ai/api/v1/chat/completions`
- **Data Path**: `data/reviews.csv`

## Deployment

### Streamlit Cloud Deployment
1. Push code to GitHub
2. Visit https://streamlit.io/cloud
3. Create new app from repository
4. Add `OPENROUTER_API_KEY` in Streamlit Cloud secrets
5. Deploy both user_app.py and admin_app.py as separate apps

### Environment Setup
The system uses environment variables for security:
- `OPENROUTER_API_KEY`: Required for LLM API calls

## Error Handling

- API timeouts: 30-second timeout configured
- Empty reviews: Validation prevents empty submissions
- Missing dependencies: Clear error messages from pip
- API failures: HTTP error status codes are propagated

## Testing

Run the test app to verify Streamlit installation:
```bash
streamlit run test_app.py
```

## Project Structure

```
fynd-task/
├── admin_app.py           # Admin dashboard
├── user_app.py            # User feedback interface
├── utils.py               # Core utilities and LLM integration
├── prompts.py             # Prompt templates
├── requirements.txt       # Python dependencies
├── readme.txt             # Project overview
├── test_app.py            # Streamlit test
├── SUBMISSION.md          # This file
├── .gitignore             # Git ignore rules
├── data/
│   └── reviews.csv        # Feedback storage (auto-created)
└── __pycache__/
```

## Notes

- API keys are never stored in code - always use environment variables
- The system is stateless and can be scaled horizontally
- Data is stored locally; consider a database for production
- The Mistral model provides good balance of speed and quality
- Customizable prompts allow for domain-specific responses

## Future Enhancements

- Database integration (PostgreSQL/MongoDB)
- Multi-language support
- Advanced sentiment analysis
- Custom model selection
- Rate limiting and throttling
- User authentication for admin dashboard
- Bulk feedback export functionality
- Real-time notifications for critical feedback

## Support

For questions or issues:
1. Check that `OPENROUTER_API_KEY` is properly set
2. Verify internet connectivity for API calls
3. Check Streamlit version compatibility
4. Review error messages in terminal output

---

**Submission Date**: December 15, 2025  
**Status**: Ready for Production
