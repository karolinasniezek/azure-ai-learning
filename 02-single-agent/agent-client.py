import os

from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

load_dotenv()

PROJECT_ENDPOINT = os.getenv("PROJECT_ENDPOINT")
AGENT_NAME = os.getenv("AGENT_NAME")

with (
    DefaultAzureCredential() as credential,
    AIProjectClient(
        endpoint=PROJECT_ENDPOINT,
        credential=credential,
        allow_preview=True,
    ) as project_client,
):
    print("✅ Connected to Azure AI Foundry!")

    agent = project_client.agents.get(agent_name=AGENT_NAME)

    agent_version = agent.versions["latest"].version
    print(f"Using version: {agent_version}")

    openai_client = project_client.get_openai_client(
        agent_name=AGENT_NAME
    )

    response = openai_client.responses.create(
        input="What is Azure AI Foundry?"
    )

    print(response.output_text)