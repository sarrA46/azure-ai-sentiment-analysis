import os
from collections import Counter

from dotenv import load_dotenv
from azure.cosmos import CosmosClient
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

load_dotenv()
cosmos = CosmosClient(os.environ["COSMOS_URI"], credential=os.environ["COSMOS_KEY"])
container = cosmos.get_database_client("sentiment-db").get_container_client("analyses")


def load_docs():
    query = "SELECT c.id, c.language, c.text, c.sentiment, c.key_phrases FROM c"
    return list(container.query_items(query, enable_cross_partition_query=True))


def detect_themes(docs, n_clusters=5, top_n=3):
    docs = [d for d in docs if d.get("key_phrases")]
    if len(docs) < n_clusters:
        raise ValueError(f"Pas assez de documents ({len(docs)}) pour {n_clusters} thèmes")

    corpus = [" ".join(d["key_phrases"]).lower() for d in docs]
    X = TfidfVectorizer().fit_transform(corpus)
    model = KMeans(n_clusters=n_clusters, n_init=10, random_state=42)
    labels = model.fit_predict(X)

    themes = {}
    for doc, lab in zip(docs, labels):
        themes.setdefault(int(lab), []).append(doc)

    result = []
    for lab, items in sorted(themes.items()):
        counter = Counter(p.lower() for d in items for p in d["key_phrases"])
        result.append({
            "theme": lab,
            "label": ", ".join(p for p, _ in counter.most_common(top_n)),
            "count": len(items),
            "negative": sum(1 for d in items if d["sentiment"] == "negative"),
            "examples": [d["text"] for d in items[:2]],
        })
    return result


if __name__ == "__main__":
    docs = load_docs()
    print(len(docs), "documents chargés")
    for lang in ("fr", "en", "ar"):
        sous_docs = [d for d in docs if d["language"] == lang]
        print(f"\n===== Langue : {lang} ({len(sous_docs)} docs) =====")
        try:
            for t in detect_themes(sous_docs, n_clusters=3):
                print(f"\nThème {t['theme']} : {t['label']}  ({t['count']} docs, {t['negative']} négatifs)")
                for ex in t["examples"]:
                    print("   -", ex)
        except ValueError as e:
            print("   ", e)