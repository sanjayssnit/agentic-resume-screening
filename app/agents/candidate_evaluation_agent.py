from openai import OpenAI
from dotenv import load_dotenv
import os
from app.prompts import CANDIDATE_EVALUATION
import json

client = OpenAI()

def evaluate_candidate(candidate_details: str, jd: str) -> str:
    """
    Function to analyze the extracted text from a resume using OpenAI's API.
    """
    prompt = CANDIDATE_EVALUATION.format(resume_json=candidate_details, jd_json=jd)
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
        )
        print("Response from OpenAI API:", response.choices[0].message.content)
        return response.choices[0].message.content
    except Exception as e:
        return {"error": str(e)}