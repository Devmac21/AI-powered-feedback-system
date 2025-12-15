# prompts.py

def user_response_prompt(review: str) -> str:
    return f"""
You are a polite and empathetic customer support assistant.

Respond helpfully and professionally to the following customer review.

Review:
"{review}"
"""


def admin_summary_prompt(review: str) -> str:
    return f"""
Summarize the following customer review in one concise sentence.
Then suggest one clear recommended action for the business.

Review:
"{review}"
"""
