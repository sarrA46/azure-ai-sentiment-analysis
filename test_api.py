import os

os.environ.setdefault("API_KEY", "cle-de-test")

from fastapi.testclient import TestClient

import api

api.API_KEY = os.environ["API_KEY"]
client = TestClient(api.app)
HEADERS = {"x-api-key": api.API_KEY}


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_sans_cle_refuse():
    r = client.post("/classify", json={"text": "Bonjour"})
    assert r.status_code == 401


def test_mauvaise_cle_refuse():
    r = client.post("/classify", json={"text": "Bonjour"}, headers={"x-api-key": "faux"})
    assert r.status_code == 401


def test_classify():
    r = client.post(
        "/classify",
        json={"text": "Pouvez-vous m'expliquer le paiement ?"},
        headers=HEADERS,
    )
    assert r.status_code == 200
    assert r.json()["category"] == "Question"


def test_batch_trop_grand():
    r = client.post(
        "/analyze/batch", json={"texts": ["abc"] * 26}, headers=HEADERS
    )
    assert r.status_code == 400


def test_trends_parametre_invalide():
    r = client.get("/trends?days=0", headers=HEADERS)
    assert r.status_code == 400