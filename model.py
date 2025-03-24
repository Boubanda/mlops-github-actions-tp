def predict_sentiment(text):
    """
    Retourne le sentiment basé sur un texte simple.
    """
    if not text:
        return "neutral"
    if "happy" in text.lower() or "good" in text.lower():
        return "positif"
    if "sad" in text.lower() or "bad" in text.lower():
        return "negative"
    return "neutral"


def predict_sentiment(text):
    """
    Prédit un sentiment basé sur des mots-clés simples.

    Args:
        text (str): le texte à analyser

    Returns:
        str: 'positive', 'negative' ou 'neutral'
    """
