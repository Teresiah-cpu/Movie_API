from flask import render_template
from app import app

# Views
from .request import get_movies

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie )
# @app.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''

#     title = 'Home - Welcome to The best Movie Review Website Online'
#     return render_template('index.html', title = title)
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''
#     message = 'Hello World'
#     return render_template('index.html',message = message)


@app.route('/movie/<int:movie_id>')
def movie(movie_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('movie.html',id = movie_id)