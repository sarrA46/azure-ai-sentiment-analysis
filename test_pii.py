import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

load_dotenv()
client = TextAnalyticsClient(
    endpoint=os.environ["LANGUAGE_ENDPOINT"],
    credential=AzureKeyCredential(os.environ["LANGUAGE_KEY"]),
)

documents = [
    ("Bonjour, je suis Ahmed Ben Ali, mon email est ahmed.benali@gmail.com et mon tel 98 123 456.", "fr"),
    ("Please call me, I am John Smith, phone +1 555 123 4567, john@example.com", "en"),
]

for text, lang in documents:
    r = client.recognize_pii_entities([text], language=lang)[0]
    print("\nOriginal  :", text)
    if r.is_error:
        print("Erreur :", r.error.message)
        continue
    print("Anonymisé :", r.redacted_text)
    for e in r.entities:
        print(f"  - {e.text} -> {e.category} ({e.confidence_score:.2f})")