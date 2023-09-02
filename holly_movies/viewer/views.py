# builtin python

# 3rd packages

# own packages

# posegrowane alfabetycznie.
from pprint import pprint

import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView,\
    ListView, FormView, CreateView, UpdateView

from .models import Movie, Link, Genre

# NEW
from .forms import MovieForm, GenreForm, MovieFormModel
from logging import getLogger

from django.urls import reverse_lazy

LOGGER = getLogger()

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

# def movies(request):
#     movies = list(Movie.objects.all().values())
#     return JsonResponse(movies, safe=False)
#

def home(request): # /<str:s0>
    s1 = request.GET.get('s1', '') # -> /adjective?s1=xyz vs /adjective s1 = None s1=''
    return render(request, template_name='hello.html', context={'adjectives': [s1, 'beautiful', 'wonderful'],
                                                                'page_title': 'Holly Movies Home Page'})


def movies_list(request):
    return render(
        request,
        template_name='movies.html',
        context={'movies': Movie.objects.all()}
    )


class MoviesView(View):
    def get(self, request):
        return render(
            request,
            template_name='movies.html',
            context={'movies': Movie.objects.all()}
        )


class MoviesTemplateView(TemplateView):
    template_name = 'movies.html'
    extra_context = {'movies': Movie.objects.all()}


class MoviesListView(ListView):
    template_name = 'movies_list_view.html'
    model = Movie




class MyFavLinks(TemplateView):
    template_name = 'fav_links.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['links'] = Link.objects.all()
        context['title'] = 'My Fav Links'
        return context



# ---------------02.09---------------- #

class GenreCreateView(FormView): # self.form_class
    template_name = 'create_genre_form.html'
    form_class = GenreForm
    success_url = reverse_lazy('movies-list-view')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Genre.objects.create(name=cleaned_data['name'])


        return result

class MovieCreateView(FormView):
    template_name = 'form.html'
    form_class = MovieForm
    success_url = reverse_lazy('movies-list-view')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Movie.objects.create(
            title=cleaned_data['title'],
            genre=cleaned_data['genre'],
            rating=cleaned_data['rating'],
            released=cleaned_data['released'],
            description=cleaned_data['description'],
        )

        return result


    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')

        return super().form_invalid(form)


class MovieCreateViewForm(CreateView):
    template_name = 'form.html'
    form_class = MovieFormModel
    success_url = reverse_lazy('movies-list-view')

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')

        return super().form_invalid(form)


class MovieUpdateView(UpdateView):
    template_name = 'form.html'
    model = Movie
    form_class = MovieFormModel
    success_url = reverse_lazy('movies-list-view')

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')

        return super().form_invalid(form)