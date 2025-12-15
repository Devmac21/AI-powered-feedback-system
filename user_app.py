# user_app.py
import streamlit as st
from datetime import datetime, timezone
from utils import call_llm, init_store, save_entry
from prompts import user_response_prompt


st.set_page_config(page_title="User Feedback", layout="centered")
st.title("📝 Submit Your Feedback")

init_store()

rating = st.slider("Select Rating", 1, 5, 4)
review = st.text_area("Write your review")

if st.button("Submit"):
    if not review.strip():
        st.warning("Please write a review.")
    else:
        ai_response = call_llm(user_response_prompt(review))

        entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "rating": rating,
            "review": review,
            "ai_response": ai_response,
            "summary": "",
            "recommended_action": ""
        }

        save_entry(entry)

        st.success("Feedback submitted successfully!")
        st.subheader("AI Response")
        st.write(ai_response)
