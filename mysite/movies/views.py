from django.shortcuts import render, redirect
from movies.models import Movie
from .forms import MovieForm

# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context = {
        'movies':movie
    }
    return render(request,'movies/index.html',context)

def new(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:index')
    else:
        form=MovieForm()
        context = {
            'form':form
        }
        return render(request,'movies/new.html',context)

def create(request):
    form = MovieForm(request.POST)
    movie = form.save()
    return redirect('movies:index')

def detail(request,movie_pk):
    movie= Movie.objects.get(pk = movie_pk)
    context = {
        'movie':movie
    }
    return render(request,'movies/detail.html',context)

def update(request,movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance = movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:index')
    else:
        form = MovieForm( instance = movie)
        context = {
            'form':form
        }
    return render(request,'movies/new.html',context)

def delete(request,movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.delete()
    return redirect('movies:index')
