from django.db import models

class Ticker(models.Model):
    ticker = models.CharField(max_length=10)

    def __str__(self):
        name = self.ticker
        return name
