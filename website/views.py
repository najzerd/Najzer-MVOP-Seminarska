from turtle import title
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie
from website.form import AddMovieForm
from website.form import RecommendMovieForm
from website.models import Movie
from website.dex import DEXModel

# Create your views here.
def index(request):
    if(request.method == 'POST'):
        form = RecommendMovieForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            request.session['data'] = data
            return redirect(evaluate)
    else:
        form = RecommendMovieForm()
    return render(request, "website/index.html", {'form': form})

def movies(request):
    movie_list = Movie.objects.all()
    return render(request, "website/movies.html", {'movie_list':movie_list})

def add(request):
    if(request.method == 'POST'):
        form = AddMovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(movies)
    else:
        form = AddMovieForm()
    return render(request, "website/add.html", {'form': form})

def evaluate(request):
    data = request.session.get('data')
    movie_list = Movie.objects.all()
    evaluation_list = []

    for movie in movie_list:
        score = 0
        if int(data['year'] or 0) != 0:
            year = abs(int(data['year'] or 0) - movie.year)
            if year < 3:
                score += 10
            elif year < 6:
                    score += 8
            elif year < 9:
                    score += 6
            elif year < 12:
                    score += 4
            elif year < 15:
                    score += 2
        else:
            year = None
        
        if int(data['length'] or 0) != 0:
            duration = abs(int(data['length'] or 0) - movie.length)
            if duration < 15:
                score += 20
            elif duration < 30:
                    score += 15
            elif duration < 45:
                    score += 10
            elif duration < 60:
                    score += 5
        else:
            duration = None

        if data['geners'] == movie.geners:
            geners = True
            score += 10
        else:
            geners = False

        if str(data['director']) != "":
            if str(data['director']) == movie.director:
                director = True
                score += 5
            else:
                director = False
        else:
            director = None
        
        if data['language'] == movie.language:
            language = True
            score += 20
        else:
            language = False

        if str(data['star']) != "":
            if str(data['star']) == movie.star:
                star = True
                score += 5
            else:
                star = False
        else:
            star = None

        if float(data['rating'] or 0) != 0:
            rating = abs(float(data['rating'] or 0) - movie.rating)
            if rating < 1:
                score += 10
            elif rating < 2:
                    score += 8
            elif rating < 3:
                    score += 6
            elif rating < 4:
                    score += 4
            elif rating < 5:
                    score += 2
        else:
            rating = None
        
        if data['true_story'] == movie.true_story:
            true_story = True
            score += 5
        else:
            true_story = False
        
        if data['franchise'] == movie.franchise:
            franchise = True
            score += 5
        else:
            franchise = False

        if data['hollywood'] == movie.hollywood:
            hollywood = True
            score += 5
        else:
            hollywood = False
        
        if data['cult'] == movie.cult:
            cult = True
            score += 5
        else:
            cult = False
        
        evaluation = {
            "title": movie.title,
            "score": score,
            "year": year,
            "length": duration,
            "geners": geners,
            "director": director,
            "language": language,
            "star": star,
            "rating": rating,
            "true_story": true_story,
            "franchise": franchise,
            "hollywood": hollywood,
            "cult": cult,
        }

        evaluation_list.append(evaluation)
    sorted_list = sorted(evaluation_list, key=lambda d: d["score"], reverse=True)
    return render(request, "website/evaluate.html", {'evaluation_list':sorted_list})
