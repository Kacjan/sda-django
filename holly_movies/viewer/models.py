from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, models.DO_NOTHING, null=True)
    rating = models.IntegerField(null=True)
    released = models.DateField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Link(models.Model):
    name = models.CharField(max_length=50)
    URL = models.URLField(max_length=100, null=True)

    def __str__(self):
        return self.name

#########----------##########

















# TODO Nowy Model obojętnie jaki -> Minimum 6 pól. + Wytworzyć i przeprowadzić migrację.


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    genre = models.CharField(max_length=50)
    pages = models.PositiveIntegerField() # Tylko mógł zapisać liczby całkowite dodatnie.
    description = models.TextField()
