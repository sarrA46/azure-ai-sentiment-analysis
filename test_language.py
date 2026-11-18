from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
from cleaning import clean_text

ENDPOINT = "https://analyse-sentiment.cognitiveservices.azure.com/"
KEY = "EfWw0KILPdQvxQg3yi11pkZWfRsOejUeKbnbiId4nA9VGkqxcjw8JQQJ99CIACYeBjFXJ3w3AAAEACOGelrL"


client = TextAnalyticsClient(
    endpoint=ENDPOINT,
    credential=AzureKeyCredential(KEY),
)

raw_texts = [
    "<p>La livraison était très lente 😡 https://exemple.com</p>",
    "@smartovate The support team was really helpful! 👍",
    "الخدمة ممتازة لكن السعر مرتفع جدا",
]

# 1. نظّفو النصوص
documents = [clean_text(t) for t in raw_texts]

# 2. نكتشفو اللغة
results = client.detect_language(documents)

for doc in results:
    if doc.is_error:
        print("Erreur :", doc.error.code, doc.error.message)
        continue
    lang = doc.primary_language
    print(f"\nTexte    : {documents[int(doc.id)]}")
    print(f"Langue   : {lang.name} ({lang.iso6391_name})")
    print(f"Confiance: {lang.confidence_score:.2f}")