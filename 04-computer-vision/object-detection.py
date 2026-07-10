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

with open("images/devon.jpg", "rb") as image:

    result = client.analyze(
        image_data=image,
        visual_features=[
            VisualFeatures.OBJECTS
        ]
    )

print("=" * 20)
print("OBJECT DETECTION")


for obj in result.objects.list:
    print(f"Object: {obj.tags[0].name}")
    print(f"Confidence: {obj.tags[0].confidence:.2f}")
    print()