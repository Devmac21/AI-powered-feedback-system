# utils.py
import os
import requests
import pandas as pd
from datetime import datetime

# ----------------------------
# CONFIG
# ----------------------------
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Stable instruct model on OpenRouter
MODEL = "mistralai/mistral-7b-instruct"

DATA_PATH = "data/reviews.csv"


# ----------------------------
# LLM CALL
# ----------------------------
def call_llm(prompt: str) -> str:
    if not OPENROUTER_API_KEY:
        return "ERROR: OPENROUTER_API_KEY not set"

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a helpful customer support assistant. "
                    "Always respond politely, clearly, and professionally to user feedback."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7,
        "max_tokens": 300
    }

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://streamlit.app",
                "X-Title": "Fynd Feedback App"
            },
            json=payload,
            timeout=30
        )

        if response.status_code != 200:
            return f"LLM ERROR {response.status_code}: {response.text}"

        data = response.json()
        choices = data.get("choices", [])

        if not choices:
            return "LLM ERROR: No choices returned"

        content = choices[0].get("message", {}).get("content", "").strip()

        if not content:
            # Defensive handling for real LLM empty outputs
            return "Thank you for your feedback! Our team will review it and work on improvements."

        # Clean known Mistral formatting tokens
        return (
            content
            .replace("<s>", "")
            .replace("</s>", "")
            .replace("[OUT]", "")
            .replace("[/OUT]", "")
            .strip()
        )

    except Exception as e:
        return f"LLM EXCEPTION: {e}"


# ----------------------------
# STORAGE HELPERS
# ----------------------------
def init_store():
    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(DATA_PATH):
        df = pd.DataFrame(columns=[
            "timestamp",
            "rating",
            "review",
            "ai_response",
            "summary",
            "recommended_action"
        ])
        df.to_csv(DATA_PATH, index=False)


def save_entry(entry: dict):
    df = pd.read_csv(DATA_PATH)
    df = pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
    df.to_csv(DATA_PATH, index=False)


def load_entries():
    return pd.read_csv(DATA_PATH)
