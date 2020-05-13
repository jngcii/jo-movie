import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from reviews.forms import ReviewForm
# Create your views here.

def index(request):
    movies = Movie.objects.all()[:10]
    for m in movies:
        print(m.id)
        print(m.title)
        print(m.rank)
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



def scrap(request):

    json_path = 'https://yts.mx/api/v2/list_movies.json?page=1&limit=50'
    r = requests.get(json_path, auth=('user','pass'))
    a = r.json()['data']['movies']
    for ai in a:
        summary = ai['summary']
        title = ai['title']
        url = ai['medium_cover_image']
        try:
            Movie.objects.get(title=title)
            continue
        except Movie.DoesNotExist:
            Movie.objects.create(title=title, description=summary, poster=url)

    return redirect('index')