from django.contrib import admin

# Register your models here.
from .models import Movie, Genre, Actor

admin.site.register(Movie)
