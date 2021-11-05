from django.shortcuts import render
from django.shortcuts import HttpResponse

from .models import Actor, Genre, Movie

# Create your views here.
def details_view(request, my_id):
    obj = Movie.objects.get(id=my_id)
    context = {
        'object':obj
    }
    #return HttpResponse("hello")
    return render(request,"details.html",context)

def all_movies_view(request):
    movies = Movie.objects.all()
    actors = Actor.objects.all()
    genres = Genre.objects.all()
    context = {
        "movies": movies,
        "actors": actors,
        "genres": genres
    }

    return render(request,"search.html", context)