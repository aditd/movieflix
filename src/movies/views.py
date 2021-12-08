from django.shortcuts import render
from django.shortcuts import HttpResponse
from django import forms

from .models import Actor, Genre, Movie

class search(forms.Form):
    actor = forms.CharField(max_length=100, required=False)
    director = forms.CharField(max_length=100, required=False)
    genre = forms.CharField(max_length=60, required=False)

# Create your views here.
def details_view(request, my_id):
    obj = Movie.objects.get(id=my_id)
    context = {
        'object':obj
    }
    print(my_id)
    #return HttpResponse("hello")
    return render(request,"details.html",context)

def all_movies_view(request):
    if request.method == 'GET':
        form = search(request.GET)
        x = Movie.objects.all()
        if form.is_valid():
            if form.cleaned_data['director'] != '':
                x = x.filter(directors__name=form.cleaned_data['director'].title())
            if form.cleaned_data['actor'] != '':
                x = x.filter(actors__name=form.cleaned_data['actor'].title())
            if form.cleaned_data['genre'] != '':
                x = x.filter(genre__name=form.cleaned_data['genre'].title())


        #actor = form.cleaned_data['actor']
        #actor = form.cleaned_data['genre']

    #movies = Movie.objects.all()
    #actors = Actor.objects.all()
    #genres = Genre.objects.all()
    context = {
        "movies": x,
        #"actors": actors,
        #"genres": genres,
        "form": form
    }

    return render(request,"search.html", context)