from django.forms import ModelForm
from sentanalysis.models import SentimentIdentifier
from django import forms

class SentimentIdentifierForm(forms.ModelForm):
    class Meta:
        model = SentimentIdentifier
        fields = (
            'sentiment',
        )

        labels = {
            'sentiment': 'Sentiment',
        }

        widgets = {
            'sentiment': forms.TextInput(attrs={'placeholder': 'Enter a sentiment...'}),
        }
