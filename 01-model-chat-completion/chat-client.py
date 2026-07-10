from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

endpoint = os.getenv("AZURE_FOUNDRY_ENDPOINT")
api_key = os.getenv("AZURE_FOUNDRY_API_KEY")
deployment_name = os.getenv("AZURE_FOUNDRY_MODEL")

print(endpoint)
print(deployment_name)
client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

response = client.responses.create(
    model=deployment_name,
    input="What is Azure AI Foundry?"
)

print(response.output_text)