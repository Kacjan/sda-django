from django.shortcuts import render

from django.http import HttpResponse
from pprint import pprint
from .models import Movie

def hello(request, pk):
    # if s == 'signed':
    #     pass
    movies = list(Movie.objects.all().values_list('title', 'genre'))
    print(movies)
    return HttpResponse(f'Hello, world! My fav movie is: {movies}')


def hello_1(request):
    arr = [1, 7, -33, 11, 33]
    sort = request.GET.get('sort', '')
    if sort == 'true':
        return HttpResponse(" ".join(str(sorted(arr))))

    return HttpResponse(" ".join(str(arr)))