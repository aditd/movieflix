from typing_extensions import runtime
from django.db import models

#Movie.objects.create(title=data[i]['title'], rating=data[i]['rating'],year=data[i]['year'], genre= ','.join(data[i]['genre']),actors=','.join(data[i]['actors']),directors=','.join(data[i]['directors']),runtime = data[i]['runtime'], certificate = data[i]['certificate'], icon_url=data[i]['icon_url'],big_poster_url = data[i]['big_poster_url'],poster_url = data[i]['poster_url'])
#genre

# Create your models here.
class Movie(models.Model):
    title       = models.CharField(max_length=100)
    runtime     = models.IntegerField()
    year        = models.IntegerField()
    rating      = models.DecimalField(decimal_places=1,max_digits=2)
    genre       = models.TextField(null=True)
    directors   = models.TextField()
    actors      = models.TextField()
    certificate = models.TextField(max_length=4)
    icon_url    = models.SlugField(max_length=220, null=True)
    poster_url  = models.SlugField(max_length=220, null=True)
    big_poster_url = models.SlugField(max_length=220, null=True)