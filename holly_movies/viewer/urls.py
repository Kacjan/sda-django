from django.urls import path

from .views import hello, home, MoviesView, MoviesTemplateView, \
    MoviesListView, MyFavLinks, MovieCreateViewForm, GenreCreateView, MovieUpdateView, MovieDeleteView


urlpatterns = [
    path('hello/<int:pk>', hello),
    path('adjectives/', home, name='hello'),
    path('', MoviesView.as_view(), name='index'),
    path('movies/template', MoviesTemplateView.as_view(), name='movies-template'),
    path('movies/list_view', MoviesListView.as_view(), name='movies-list-view'),
    path('links', MyFavLinks.as_view(), name='links'),
    path('movies/create', MovieCreateViewForm.as_view(), name='movie_create'),
    path('movies/create/genre', GenreCreateView.as_view(), name='genre_create'),
    path('movies/update/<pk>', MovieUpdateView.as_view(), name='movie_update'),
    path('movies/delete/<pk>', MovieDeleteView.as_view(), name='movie_delete'),
]