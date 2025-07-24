from openai import OpenAI
from dotenv import load_dotenv
import os
from app.prompts import EXTRACT_JD_DETAILS
import json

client = OpenAI()

def analyze_jd(text: str) -> str:
    """
    Function to analyze the extracted text from a job description using OpenAI's API.
    """
    prompt = EXTRACT_JD_DETAILS.format(jd_text=text)
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
        )
        print("Response from OpenAI API for JD:", response.choices[0].message.content)
        return response.choices[0].message.content
    except Exception as e:
        return {"error": str(e)}
    





