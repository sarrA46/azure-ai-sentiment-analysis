import pipeline

textes = [
    "La livraison était très lente, j'ai attendu deux semaines",
    "Livraison rapide et colis bien emballé",
    "Le livreur est arrivé en retard, très déçu",
    "Le prix est trop élevé pour la qualité proposée",
    "Bon rapport qualité prix, je recommande",
    "Trop cher par rapport à la concurrence",
    "Le service client ne répond jamais à mes emails",
    "Support client très réactif et aimable",
    "Impossible de joindre le service après-vente",
    "The delivery was late and the package was damaged",
    "Fast shipping, arrived a day early",
    "Delivery took forever, very disappointed",
    "The price is too high for what you get",
    "Great value for money, totally worth it",
    "Too expensive compared to other brands",
    "Customer support never answered my questions",
    "The support team was really helpful and kind",
    "I could not reach anyone at customer service",
    "The battery life is great and the screen is sharp",
    "The screen cracked after a week, poor quality",
    "La qualité du produit est excellente, très solide",
    "Produit de mauvaise qualité, il est tombé en panne",
    "التوصيل كان بطيئا جدا وتأخر الطلب",
    "السعر مرتفع جدا مقارنة بالجودة",
    "خدمة العملاء ممتازة وسريعة الرد",
    "جودة المنتج ممتازة وأنصح به",
]

for i in range(0, len(textes), 25):
    res = pipeline.process_batch(textes[i:i + 25], source="seed")
    print(len(res), "documents enregistrés")