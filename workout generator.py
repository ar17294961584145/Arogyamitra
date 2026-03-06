import os
from langchain_openai import ChatOpenAI
from langchain.prompts import promptTemplate
from dotenv import load_dotenv
from logger import log_message

load dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in .env")

    11m=ChatopenAI(model="gpt-4",temparature=0.7)