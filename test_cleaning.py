from cleaning import clean_text


def test_html_removed():
    assert clean_text("<p>Bonjour <b>monde</b></p>") == "Bonjour monde"


def test_html_entities():
    assert clean_text("Prix &amp; qualité") == "Prix & qualité"


def test_url_removed():
    assert clean_text("Voir https://exemple.com/page ici") == "Voir ici"


def test_mention_removed():
    assert clean_text("@smartovate merci beaucoup") == "merci beaucoup"


def test_hashtag_keeps_word():
    assert clean_text("Livraison nulle #déçu") == "Livraison nulle déçu"


def test_emoji_removed():
    assert clean_text("Super produit 😍👍") == "Super produit"


def test_extra_spaces():
    assert clean_text("trop    d'espaces   ici") == "trop d'espaces ici"



def test_empty_and_none():
    assert clean_text("") == ""
    assert clean_text(None) == ""


def test_arabic_preserved():
    assert clean_text("الخدمة ممتازة 😍") == "الخدمة ممتازة"