from django.db import models

# Create your models here.
class CountryData(models.Model):
    country = models.CharField(max_length=100)
    population = models.IntegerField()

    def __str__(self) :
        return f'{self.country}-{self.population}'