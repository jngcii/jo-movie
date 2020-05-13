import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from reviews.forms import ReviewForm
# Create your views here.

def index(request):
    movies = Movie.objects.all()[:10]
    context = {
        'movies': movies,
    }
    return render(request, 'movies/main.html', context)

def search(request):
    keyword = request.GET['keyword']
    print(keyword)
    movies = Movie.objects.filter(title__icontains=keyword)
    print(movies)
    context = {
        'movies':movies
    }
    return render(request, 'movies/main.html', context)

def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    form = ReviewForm()

    context = {
        'movie':movie,
        'form':form,
    }
    return render(request, 'movies/detail.html', context)



# def scrap(request):

#     json_path = 'https://yts.mx/api/v2/list_movies.json?page=1&limit=50'
#     r = requests.get(json_path, auth=('user','pass'))
#     a = r.json()['data']['movies']
#     for ai in a:
#         summary = ai['summary']
#         title = ai['title']
#         url = ai['medium_cover_image']
#         try:
#             Movie.objects.get(title=title)
#             continue
#         except Movie.DoesNotExist:
#             Movie.objects.create(title=title, description=summary, poster=url)

#     return redirect('index')

def scrap(request):
    ## origin code #
    # r = requests.get(json_path, auth=('user','pass'))
    # a = r.json()['data']['movies']

    ## new code
    # 한 페이지당 20개씩 끊어짐
    lang ='ko-KR'
    TMDb_key = 'f790c6911bd5abe1dd9098d76849459f'
    poster_base_url= 'https://image.tmdb.org/t/p/w500/'
    discover_url = f'https://api.themoviedb.org/3/discover/movie?api_key={TMDb_key}&language={lang}&sort_by=popularity.desc&include_adult=false&include_video=false&page=1'
    json_data = requests.get(discover_url).json()
    json_path = 'https://yts.mx/api/v2/list_movies.json?page=1&limit=50'
    
    movies = json_data['results']
    
    for idx, m in enumerate(movies):
        if type(m) == tuple:
            break
        url = f'{poster_base_url}{m["poster_path"]}'
        title = m['title']
        summary = m['overview']
        # m_score = m['vote_average'] # rank data
        try:
            Movie.objects.get(title=title)
            continue
        except Movie.DoesNotExist:
            Movie.objects.create(title=title, description=summary, poster=url)
    return redirect('index')