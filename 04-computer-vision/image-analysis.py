import os

from dotenv import load_dotenv

from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures

load_dotenv()

endpoint = os.getenv("AZURE_VISION_ENDPOINT")
key = os.getenv("AZURE_VISION_KEY")

client = ImageAnalysisClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

print("✅ Connected to Azure AI Vision!")

with open("images/devon-rex.jpg", "rb") as image:

    result = client.analyze(
        image_data=image,
        visual_features=[
            VisualFeatures.CAPTION,
            VisualFeatures.TAGS,
            VisualFeatures.OBJECTS,
            VisualFeatures.READ
        ]
    )

print("=" * 20)
print("CAPTION")

if result.caption:
    print(result.caption.text)
    print(f"Confidence: {result.caption.confidence:.2f}")

print("\n")

print("=" * 20)
print("TAGS")

for tag in result.tags.list:
    print(f"{tag.name} ({tag.confidence:.2f})")

print("\n")

print("=" * 20)
print("OBJECTS")

for obj in result.objects.list:
    print(f"{obj.tags[0].name} ({obj.tags[0].confidence:.2f})")

print("\n")

print("=" * 20)
print("OCR")

if result.read:

    for block in result.read.blocks:
        for line in block.lines:
            print(line.text)