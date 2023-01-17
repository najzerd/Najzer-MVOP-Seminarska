from django import forms
from django.forms import ModelForm

from website.models import Movie

class AddMovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'year', 'length', 'geners', 'director', 'language', 'star', 'rating', 'true_story', 'franchise', 'hollywood', 'cult')

    title = forms.CharField(label='Movie Title', max_length=100)
    year = forms.IntegerField(label='Year of release')
    length = forms.IntegerField(label='Duration in minutes')

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
    geners = forms.ChoiceField(label='Gener', choices=GENERS)
    director = forms.CharField(label='Movie Director')

    LANGUAGE = (
        ('en', 'English'),
        ('sl', 'Slovene'),
        ('ge', 'German'),
        ('dk', 'Danish'),
    )
    language = forms.ChoiceField(label='Movie language', choices=LANGUAGE)
    star=forms.CharField(label = 'Star of the film')
    rating = forms.FloatField(label= 'IMDB rating of the movie')
    true_story = forms.BooleanField(required=False, label='Is the movie based on a true story')
    franchise = forms.BooleanField(required=False, label='Is the movie part of a franchise')
    hollywood = forms.BooleanField(required=False, label='Is it a Hollywood movie')
    cult = forms.BooleanField(required=False, label='Does the movie have a cult status')

class RecommendMovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('year', 'length', 'geners', 'director', 'language', 'star', 'rating', 'true_story', 'franchise', 'hollywood', 'cult')

    year = forms.IntegerField(label='Year of release', required=False)
    length = forms.IntegerField(label='Duration in minutes', required=False)

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
    geners = forms.ChoiceField(label='Gener', choices=GENERS)
    director = forms.CharField(label='Movie Director', required=False)

    LANGUAGE = (
        ('en', 'English'),
        ('sl', 'Slovene'),
        ('ge', 'German'),
        ('dk', 'Danish'),
    )
    language = forms.ChoiceField(label='Movie language', choices=LANGUAGE)
    star=forms.CharField(label = 'Star of the film', required=False)
    rating = forms.FloatField(label= 'IMDB rating of the movie', required=False)
    true_story = forms.BooleanField(required=False, label='Is the movie based on a true story')
    franchise = forms.BooleanField(required=False, label='Is the movie part of a franchise')
    hollywood = forms.BooleanField(required=False, label='Is it a Hollywood movie')
    cult = forms.BooleanField(required=False, label='Does the movie have a cult status')