import os

from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

load_dotenv()

endpoint = os.getenv("AZURE_LANGUAGE_ENDPOINT")
key = os.getenv("AZURE_LANGUAGE_KEY")

credential = AzureKeyCredential(key)

client = TextAnalyticsClient(
    endpoint=endpoint,
    credential=credential
)

documents = [
    "Microsoft Build 2026 introduced new Azure AI Foundry features for developers."
]

response = client.extract_key_phrases(documents)

for document, result in zip(documents, response):

    print(f"Text:\n{document}")

    print("\nKey phrases:")

    for phrase in result.key_phrases:
        print(f"• {phrase}")