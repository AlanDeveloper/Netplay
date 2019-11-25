from flask import Blueprint, Flask, render_template, request, redirect, session, jsonify
from app.models.film_user import film_user
from app.models.serie_user import serie_user
from app.models.episode import episode
from app.models.serie import serie
from app.models.film import film
from app.models import __init__

from app import db

control = Blueprint('control', __name__, url_prefix='/')

@control.route('/')
def index():
    return render_template('user/login.html')

@control.route('/home', methods=['GET', 'POST'])
def home():
    list_films_active = film.ls()
    list_serie_active = serie.ls()

    if session['admin']:
        return render_template('printer/home.html', ls_films_active=list_films_active, ls_series_active=list_serie_active)
    else:
        items = []
        items2 = []
        items3 = []
        ls_films = film_user.searchFilms(session['id'])
        ls_series = serie_user.searchseries(session['id'])

        for item in ls_films:
            if film_user.search(item.film_id, session['id']).watched != True:
                f = film.search(item.film_id)
                items.append(f)

        for item in ls_series:
            s = episode.search_episode(item.serie_id, item.season_id, item.episode_id)
            s2 = serie.search(item.serie_id)
            if item.watched != True:
                items2.append(s2)
                items3.append(s)
        return render_template('printer/home.html', ls_films=items, ls_series=items2, ls_episodes=items3, ls_films_active=list_films_active, ls_series_active=list_serie_active)

@control.route('/assistidos', methods=['POST'])
def watching():
    user_id = int(session['id'])
    video_id = int(request.form['video'])
    time = request.form['time']
    
    watched = request.form['watched']
    if watched == 'true':
        watched = True
    else:
        watched = False

    t = request.form['type'] 
    if t == 'filme':
        f = film_user.search(video_id, user_id)

        if f:
            f.time = time
            f.watched = bool(watched)
            film_user.update(f)
        else:
            f = film_user(video_id, user_id, time)
            f.watched = bool(watched)
            film_user.add(f)
        return jsonify({'response': True})
    else:
        serie_id = int(request.form['serie'])
        season_id = int(request.form['season'])

        s = serie_user.search(serie_id, season_id, video_id, user_id)
        if s:
            s.time = time
            s.watched = bool(watched)
            serie_user.update(s)
        else:
            s = serie_user(serie_id, season_id, video_id, user_id, time)
            s.watched = bool(watched)
            serie_user.add(s)
        return jsonify({'response': True})

@control.route('/tempo', methods=['POST'])
def time_watch():
    user_id = int(session['id'])
    video_id = int(request.form['video'])
    
    t = request.form['type']
    if t == 'filme':
        f = film_user.search(video_id, user_id)
        if f:
            return jsonify({'time': f.time})
        else:
            return jsonify({'time': 0})
    else:
        serie_id = int(request.form['serie'])
        season_id = int(request.form['season'])

        s = serie_user.search(serie_id, season_id, video_id, user_id)
        if s:
            return jsonify({'time': s.time})
        else:
            return jsonify({'time': 0})

@control.route('/selecionar_filmes', methods=['GET', 'POST'])
def select_film():
    ls = film.ls()
    if request.method == 'POST':
        checkbox = request.form.getlist('select')

        for film_list in ls:
            for box_film in checkbox:
                if film_list.id == box_film:
                    film_list.id = None

            if film_list.id != None:
                film_list.active = False
                film.update(film_list)

        for film_id in checkbox:
            f = film.search(film_id)
            f.active = True    
            film.update(f)
            
        return redirect('/')
    else:

        return render_template('printer/select_film.html', ls=ls)

@control.route('/selecionar_series', methods=['GET', 'POST'])
def select_serie():
    ls = serie.ls()
    if request.method == 'POST':
        checkbox = request.form.getlist('select')

        for serie_list in ls:
            for box_serie in checkbox:
                if serie_list.id == box_serie:
                    serie_list.id = None

            if serie_list.id != None:
                serie_list.active = False
                serie.update(serie_list)

        for serie_id in checkbox:
            f = serie.search(serie_id)
            f.active = True
            serie.update(f)

        return redirect('/')
    else:

        return render_template('printer/select_serie.html', ls=ls)
