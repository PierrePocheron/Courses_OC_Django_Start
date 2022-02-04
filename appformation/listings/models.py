from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):

  def __str__(self):
    return f'{self.name}'

  class Genre(models.TextChoices):
    HIP_HOP = 'HH'
    SYNTH_POP = 'SP'
    ALTERNATIVE_ROCK = 'AR'

  name = models.fields.CharField(max_length=100)
  genre = models.fields.CharField(choices=Genre.choices, max_length=5)
  biography = models.fields.CharField(max_length=1000)
  year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2021)])
  publication_date = models.fields.DateField(null=True,blank=True)
  official_homepage = models.fields.URLField(null=True, blank=True)

class Listing(models.Model):

  def __str__(self):
    return f'{self.title}'

  title = models.fields.CharField(max_length=100)
  description = models.fields.CharField(max_length=5000)
  sold = models.fields.BooleanField()
  year = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2050)])
  type = models.fields.CharField(max_length=100)
  band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
