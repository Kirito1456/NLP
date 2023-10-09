from django.apps import AppConfig
from django.conf import settings
import joblib
import os
import spacy  # Import spaCy


# Load spaCy's English tokenizer and stop words
nlp = spacy.load("en_core_web_sm")

# Text preprocessing using spaCy
def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if (token.text.lower() == "not" or (not token.is_stop and token.is_alpha))]
    return ' '.join(tokens)



class SentanalysisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sentanalysis'

    preprocess = preprocess_text
    
    # Load joblib files
    model = joblib.load(os.path.join(settings.BASE_DIR, 'models/final_model.joblib'))
    calibrated_clf = joblib.load(os.path.join(settings.BASE_DIR, 'models/calibrated_classifier.joblib'))
    vectorizer = joblib.load(os.path.join(settings.BASE_DIR, 'models/tfidf_vectorizer.joblib'))