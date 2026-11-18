import json
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, f1_score
from sklearn.pipeline import make_pipeline

LABELS = ["Reclamation", "Suggestion", "Question", "Compliment", "Urgence"]

with open("dataset_classification.json", encoding="utf-8") as f:
    data = json.load(f)

# Même découpage que pour Azure : 1 exemple sur 5 = test
train = [d for i, d in enumerate(data) if i % 5 != 0]
test = [d for i, d in enumerate(data) if i % 5 == 0]

X_train = [d["text"] for d in train]
y_train = [d["category"] for d in train]
X_test = [d["text"] for d in test]
y_test = [d["category"] for d in test]

model = make_pipeline(
    TfidfVectorizer(analyzer="char_wb", ngram_range=(2, 5), sublinear_tf=True),
    LogisticRegression(max_iter=1000),
)
model.fit(X_train, y_train)

pred = model.predict(X_test)

print(f"Train : {len(train)} exemples | Test : {len(test)} exemples\n")
print(classification_report(y_test, pred, labels=LABELS, digits=3))
print("F1 macro :", round(f1_score(y_test, pred, average="macro"), 3))

print("\nMatrice de confusion (lignes = réel, colonnes = prédit) :")
print("Ordre :", LABELS)
print(confusion_matrix(y_test, pred, labels=LABELS))

joblib.dump(model, "classifier.joblib")
print("\nModèle sauvegardé : classifier.joblib")

# Test sur de nouvelles phrases
exemples = [
    "Le colis est arrivé cassé, je suis très mécontent",
    "Pouvez-vous me dire quand ma commande arrive ?",
    "Super service, merci à toute l'équipe",
    "URGENT mon compte est bloqué aidez-moi",
    "Vous devriez ajouter le paiement par carte",
]
print("\nTest sur de nouvelles phrases :")
for t in exemples:
    print(f"  {model.predict([t])[0]:12s} <- {t}")