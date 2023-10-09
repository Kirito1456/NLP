from django.db import models

# Create your models here.

class SentimentIdentifier(models.Model):
    # Field to store sentiment statement
    sentiment = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.sentiment