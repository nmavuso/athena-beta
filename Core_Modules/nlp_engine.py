# Core_Modules/nlp_engine.py
import spacy

# Load a small model for demonstration. In production, you might call a large-scale model or external API.
nlp = spacy.load("en_core_web_sm")

def process_text(text):
    """
    Processes text and returns a response.
    This stub simply echoes the text.
    """
    doc = nlp(text)
    # (In a real system, you might extract intent, sentiment, etc.)
    return f"Processed text: {text}"
