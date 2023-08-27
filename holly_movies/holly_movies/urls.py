"""
URL configuration for holly_movies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from viewer.views import hello, home, movies_list, MoviesView, MoviesTemplateView\
    ,MoviesListView, MyFavLinks
#, movies

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<int:pk>', hello),
    path('adjectives/', home, name='hello'),
    # path('movies', movies),
    # path('', movies_list, name='index')
    path('', MoviesView.as_view(), name='index'),
    path('movies/template', MoviesTemplateView.as_view(), name='movies-template'),
    path('movies/list_view', MoviesListView.as_view(), name='movies-list-view'),
    path('links', MyFavLinks.as_view(), name='links') # localhost:8000/links
]
