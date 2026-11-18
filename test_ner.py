import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

load_dotenv()
client = TextAnalyticsClient(
    endpoint=os.environ["LANGUAGE_ENDPOINT"],
    credential=AzureKeyCredential(os.environ["LANGUAGE_KEY"]),
)

# (texte, langue)
documents = [
    ("J'ai acheté un iPhone à Tunis chez Tunisie Telecom le 5 juillet, la livraison était lente.", "fr"),
    ("The Samsung Galaxy screen is great, I bought it in Paris for 800 dollars.", "en"),
    ("اشتريت هاتف سامسونج من صفاقس وكانت الخدمة ممتازة", "ar"),
]

for text, lang in documents:
    print("\n" + "=" * 60)
    print("Texte :", text)

    ner = client.recognize_entities([text], language=lang)[0]
    if ner.is_error:
        print("Erreur NER :", ner.error.message)
    else:
        print("Entités :")
        for e in ner.entities:
            print(f"  - {e.text} -> {e.category} ({e.confidence_score:.2f})")

    kp = client.extract_key_phrases([text], language=lang)[0]
    if kp.is_error:
        print("Erreur phrases clés :", kp.error.message)
    else:
        print("Phrases clés :", ", ".join(kp.key_phrases))