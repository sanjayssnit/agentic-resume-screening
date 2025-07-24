from openai import OpenAI
from dotenv import load_dotenv
import os
from app.prompts import EXTRACT_CANDIDATE_DETAILS
import json

# Load environment variables from .env file
load_dotenv()
# Initialize OpenAI client with API key
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def analyze_resume(text: str) -> str:
    """
    Function to analyze the extracted text from a resume using OpenAI's API.
    """
    prompt=EXTRACT_CANDIDATE_DETAILS.format(resume_text=text)
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
        )
        print("Response from Resume Extractor Agent:", response.choices[0].message.content)
        return response.choices[0].message.content
    except Exception as e:
        return {"error": str(e)}