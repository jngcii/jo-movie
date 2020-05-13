from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie

# Create your views here.

def index(request):
    movies = Movie.objects.order_by('-rank')
    context = {
        'movies': movies,
    }
    return render(request, 'main.html', movies)


def search(request):
    # movies = Movie.objects.filter(title__icontains=)
    pass