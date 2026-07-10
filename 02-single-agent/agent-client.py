import os

from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
load_dotenv()

project_endpoint = os.getenv("PROJECT_ENDPOINT")

with (
    DefaultAzureCredential() as credential,
    AIProjectClient(
        endpoint=project_endpoint,
        credential=credential,
    ) as project_client,
):
    print("✅ Connected to Azure AI Foundry!")

    openai_client = project_client.get_openai_client()

    print("✅ OpenAI client created!")

openai_client = project_client.get_openai_client()

response = openai_client.chat.completions.create(
    model="gpt-5.4-mini",
    messages=[
        {
            "role": "user",
            "content": "Explain Azure AI Foundry in one sentence."
        }
    ]
)

print(response.choices[0].message.content) oki