# admin_app.py
import streamlit as st
from utils import load_entries, call_llm, init_store
from prompts import admin_summary_prompt

st.set_page_config(page_title="Admin Dashboard", layout="wide")
st.title("📊 Admin Dashboard")

init_store()
df = load_entries()

if df.empty:
    st.info("No feedback submissions yet.")
else:
    summaries = []
    actions = []

    for _, row in df.iterrows():
        response = call_llm(admin_summary_prompt(row["review"]))
        lines = response.split("\n")

        summaries.append(lines[0])
        actions.append(lines[-1])

    df["summary"] = summaries
    df["recommended_action"] = actions

    st.dataframe(df, use_container_width=True)

    st.subheader("📈 Rating Distribution")
    st.bar_chart(df["rating"].value_counts().sort_index())
