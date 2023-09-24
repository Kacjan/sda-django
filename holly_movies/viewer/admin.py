from django.contrib import admin

from .models import Movie, Genre, Link


admin.site.register(Genre)
admin.site.register(Link)


class MovieAdmin(admin.ModelAdmin):
    fieldsets = [
        ("None", {"fields": ["title", "created"]}),
        (
            "External Information",
            {
                "fields": ["genre", "released"],
                "description": (
                    "these fields are going to be filled with data parsed"
                    "from external database"
                ),
            },
        ),
        (
            "User Information",
            {
                "fields": ["rating", "description"],
                "description": "These fields are intended to be filled in by our users.",
            },
        ),
    ]

    readonly_fields = ["created"]

    @staticmethod
    def released_year(obj):
        return obj.released.year

    @staticmethod
    def cleanup_description(modeladmin, request, queryset):
        queryset.update(description=None)

    ordering = ["id"]
    list_display = ["id", "title", "genre", "released_year"]
    list_display_links = ["id", "title"]
    list_per_page = 20
    list_filter = ["genre"]
    search_fields = ["title"]
    actions = ["cleanup_description"]


admin.site.register(Movie, MovieAdmin)
