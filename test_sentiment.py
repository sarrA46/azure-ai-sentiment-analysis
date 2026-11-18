from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

ENDPOINT = "https://analyse-sentiment.cognitiveservices.azure.com/"
KEY = "EfWw0KILPdQvxQg3yi11pkZWfRsOejUeKbnbiId4nA9VGkqxcjw8JQQJ99CIACYeBjFXJ3w3AAAEACOGelrL"

client = TextAnalyticsClient(
    endpoint=ENDPOINT,
    credential=AzureKeyCredential(KEY),
)

documents = [
    "La qualité du produit est excellente mais la livraison était très lente.",
    "The battery life is great, but the screen is disappointing.",
    "الخدمة ممتازة لكن السعر مرتفع جدا",
]

results = client.analyze_sentiment(documents, show_opinion_mining=True)

for doc in results:
    if doc.is_error:
        print("Erreur :", doc.error.code, doc.error.message)
        continue
    print(f"\nTexte      : {documents[int(doc.id)]}")
    print(f"Sentiment  : {doc.sentiment}")
    print(f"Scores     : pos={doc.confidence_scores.positive:.2f} "
          f"neu={doc.confidence_scores.neutral:.2f} "
          f"neg={doc.confidence_scores.negative:.2f}")
    for sentence in doc.sentences:
        for opinion in sentence.mined_opinions:
            aspect = opinion.target
            avis = ", ".join(a.text for a in opinion.assessments)
            print(f"  Aspect : {aspect.text} -> {aspect.sentiment} ({avis})")