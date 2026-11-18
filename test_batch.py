import time
import pipeline

textes = [
    "La livraison était très lente",
    "Super produit, je recommande",
    "The screen is disappointing",
    "Great battery life",
    "الخدمة ممتازة",
    "السعر مرتفع جدا",
] * 4  # 24 textes

t = time.perf_counter()
res = pipeline.process_batch(textes, source="batch-test")
print(len(res), "documents traités en", round(time.perf_counter() - t, 2), "s")
print("Analyse du lot :", res[0]["analysis_seconds"], "s")
