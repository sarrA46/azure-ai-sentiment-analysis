from azure.core.exceptions import HttpResponseError
from retry import with_retry

compteur = {"n": 0}


class Fausse429(HttpResponseError):
    def __init__(self):
        super().__init__(message="Too many requests")
        self.status_code = 429


def appel_instable():
    compteur["n"] += 1
    if compteur["n"] < 3:
        raise Fausse429()
    return "OK"


def test_retry_reussit_apres_429():
    compteur["n"] = 0
    assert with_retry(appel_instable, base_delay=0.01) == "OK"
    assert compteur["n"] == 3