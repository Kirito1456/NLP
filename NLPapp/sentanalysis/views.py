from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from sentanalysis.forms import SentimentIdentifierForm
from sentanalysis.models import SentimentIdentifier
import numpy as np
from sentanalysis.apps import SentanalysisConfig

# Create your views here.

def home(request):
    template = loader.get_template("sentanalysis/home.html")
    form = SentimentIdentifierForm()
    context = {'form': form}
    return HttpResponse(template.render(context, request))

def predict(request):
    targets = ['Neutral', 'Positive', 'Negative']
    result = None
    
    if request.method == 'POST':
        form = SentimentIdentifierForm(request.POST)

        if form.is_valid():
            #print("here")
            sentiment = (form.cleaned_data.get('sentiment'))

            # Preprocess the input sentiment using SentanalysisConfig
            data = SentanalysisConfig.preprocess(sentiment)

            # Vectorize the preprocessed data
            data = SentanalysisConfig.vectorizer.transform([data])

            # Make predictions
            prediction = SentanalysisConfig.model.predict(data)[0]

            # Get prediction probabilities
            prediction_probas = SentanalysisConfig.calibrated_clf.predict_proba(data)[0]
            prediction_probas = [f"{prob * 100:.2f}%" for prob in prediction_probas]

            # Combine prediction classes with their probabilities
            prediction_probas_classes = list(zip(targets, prediction_probas))

            # Sort the predictions by probability in descending order
            prediction_probas_classes = sorted(prediction_probas_classes, key=lambda x: float(x[1][:-1]), reverse=True)

            # Map prediction to sentiment
            sentiment_map = {0: 'Neutral', 1: 'Positive', 2: 'Negative'}
            predicted_sentiment = sentiment_map.get(prediction, 'Unknown')

            result = predicted_sentiment
            
    template = loader.get_template('sentanalysis/home.html')
    context = {
        'form': form,
        'predictions': prediction_probas_classes,
        'result': result
    }
    return HttpResponse(template.render(context, request))
