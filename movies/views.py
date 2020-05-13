from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from reviews.forms import ReviewForm
# Create your views here.

def index(request):
    movies = Movie.objects.order_by('-rank')[:10]
    context = {
        'movies': movies,
    }
    return render(request, 'movies/main.html', context)

def search(request):
    keyword = request.GET.get('keyword', None)
    if not keyword:
        return redirect('index')
    
    movies = Movie.objects.filter(title__icontains=keyword)
    context = {
        'movies':movies
    }
    return render(request, 'movies/search.html', context)

def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    form = ReviewForm()

    context = {
        'movie':movie,
        'form':form,
    }
    return render(request, 'movies/detail.html', context)
