# utils.py
import os
import json
import requests
import pandas as pd
from datetime import datetime

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
}

MODEL = "mistralai/mistral-7b-instruct"
DATA_PATH = "data/reviews.csv"


def call_llm(prompt: str) -> str:
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.5,
        "max_tokens": 250
    }

    r = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=HEADERS,
        data=json.dumps(payload),
        timeout=30
    )
    r.raise_for_status()

    content = r.json()["choices"][0]["message"]["content"]
    return content.replace("<s>", "").replace("</s>", "").strip()



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
