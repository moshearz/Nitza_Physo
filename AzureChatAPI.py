import os
from openai import AzureOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Hardcoded key + endpoint
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment = os.getenv("AZURE_DEPLOYMENT")

# Setup client
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=AZURE_OPENAI_API_KEY,
    api_version="2024-05-01-preview",
)

# Chatbot function
def ask_chatbot(message: str) -> str:
    response = client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "system", "content": "H."},
            {"role": "user", "content": message}
        ],
        max_tokens=100, #lomits how long the response can be, 1000 is approxemitly 75 words
    )
    return response.choices[0].message.content

#TEST FOR THIS FILE ONLY: THE TEST WILL BE ONLY TEXT WITHOUT UI
#response = ask_chatbot("תן לי טיפ לפיזיותרפיה לשיקום הברך")
#print(response)
