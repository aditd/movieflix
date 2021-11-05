from typing_extensions import runtime
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField

#Movie.objects.create(title=data[i]['title'], rating=data[i]['rating'],year=data[i]['year'], genre= ','.join(data[i]['genre']),actors=','.join(data[i]['actors']),directors=','.join(data[i]['directors']),runtime = data[i]['runtime'], certificate = data[i]['certificate'], icon_url=data[i]['icon_url'],big_poster_url = data[i]['big_poster_url'],poster_url = data[i]['poster_url'])
#genre

class Actor(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

# Create your models here.
class Movie(models.Model):
    title       = models.CharField(max_length=100)
    runtime     = models.IntegerField(blank=True, null=True)
    year        = models.IntegerField()
    description = models.TextField(null =True)
    rating      = models.DecimalField(decimal_places=1,max_digits=2)
    genre       = models.ManyToManyField(Genre)
    directors   = models.ManyToManyField(Director)
    actors      = models.ManyToManyField(Actor)
    certificate = models.TextField(max_length=4)
    icon_url    = models.SlugField(max_length=220, null=True)
    poster_url  = models.SlugField(max_length=220, null=True)
    big_poster_url = models.SlugField(max_length=220, null=True)

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return f"/movie/{self.id}"

    def __str__(self):
        return self.title
