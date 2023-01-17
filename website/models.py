from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField(blank=False, null=True)
    length = models.IntegerField(blank=False, null=True)

    GENERS = (
        ('Action', 'Action'),
        ('Thriller', 'Thriller'),
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
        ('Comedy', 'Comedy'),
        ('Romance', 'Romance'),
        ('History', 'History'),
        ('Adventure', 'Adventure'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Fantasy', 'Fantasy'),
    )

    geners = models.CharField(max_length=50, choices=GENERS)
    director = models.CharField(max_length=50)
    
    LANGUAGE = (
        ('en', 'English'),
        ('sl', 'Slovene'),
        ('ge', 'German'),
        ('dk', 'Danish'),
    )
    language = models.CharField(max_length=50, choices=LANGUAGE)
    star = models.CharField(max_length=50)
    rating = models.FloatField(max_length=4)
    true_story = models.BooleanField(default=False)
    franchise = models.BooleanField(default=False)
    hollywood = models.BooleanField(default=False)
    cult = models.BooleanField(default=False)

    def __str__(self):
        return self.title