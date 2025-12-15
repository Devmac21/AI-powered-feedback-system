# utils.py
import os
import json
import requests
import pandas as pd
from datetime import datetime

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL = "mistralai/mistral-7b-instruct"
DATA_PATH = "data/reviews.csv"


def call_llm(prompt: str) -> str:
    if not OPENROUTER_API_KEY:
        return "ERROR: OPENROUTER_API_KEY not set"

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5,
        "max_tokens": 250
    }

    try:
        r = requests.post(
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

        if r.status_code != 200:
            return f"LLM ERROR {r.status_code}: {r.text}"

        data = r.json()
        choices = data.get("choices", [])

        if not choices:
            return "LLM ERROR: No choices returned"

        content = choices[0].get("message", {}).get("content", "")

        if not content.strip():
            return "LLM ERROR: Empty response from model"

        # 🔥 CLEAN MODEL TOKENS HERE
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
