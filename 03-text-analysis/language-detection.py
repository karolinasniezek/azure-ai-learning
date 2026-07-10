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
    "Hello! Welcome to Azure AI.",
    "Hallo! Willkommen bei Azure AI.",
    "Hallo! Welkom bij Azure AI.",
    "Bonjour! Bienvenue dans Azure AI."
]

response = client.detect_language(documents)

for document, result in zip(documents, response):
    print("-" * 40)
    print(f"Text: {document}")
    print(f"Language: {result.primary_language.name}")
    print(f"ISO Code: {result.primary_language.iso6391_name}")
    print(f"Confidence: {result.primary_language.confidence_score:.2f}")