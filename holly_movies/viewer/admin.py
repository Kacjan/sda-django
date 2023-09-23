from django.contrib import admin

from .models import Movie, Genre, Link


admin.site.register(Movie)
admin.site.register(Genre)


###
admin.site.register(Link)


# class LinkAdmin(admin.ModelAdmin):
#     list_display_links = ['id', 'name']