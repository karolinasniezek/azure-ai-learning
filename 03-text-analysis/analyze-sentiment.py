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

text = [
    "I absolutely love Azure AI Foundry. It is very easy to use!"
]

response = client.analyze_sentiment(text)[0]

print(f"Sentiment: {response.sentiment}")

print("Confidence scores:")
print(f"Positive: {response.confidence_scores.positive:.2f}")
print(f"Neutral : {response.confidence_scores.neutral:.2f}")
print(f"Negative: {response.confidence_scores.negative:.2f}")