from flask import Blueprint, Flask, render_template, request, redirect, session, jsonify
from app.models.film_user import film_user
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
        return render_template('printer/home.html', ls_film=list_films_active, ls_serie=list_serie_active)
    else:
        items = []
        ls = film_user.searchFilms(session['id'])

        for item in ls:
            if film_user.search(item.film_id, session['id']).watched != True:
                f = film.search(item.film_id)
                items.append(f)
        return render_template('printer/home.html', ls=items, ls_film=list_films_active, ls_serie=list_serie_active)

@control.route('/assistidos', methods=['POST'])
def watching():
    id = int(session['id'])
    video = int(request.form['video'])
    time = request.form['time']
    watched = request.form['watched']
    if watched == 'true':
        watched = True
    else:
        watched = False

    f = film_user.search(video, id)

    if f:
        f.time = time
        f.watched = bool(watched)
        film_user.update(f)
    else:
        f = film_user(video, id, time)
        f.watched = bool(watched)
        film_user.add(f)
    
    return jsonify({'response': True})

@control.route('/tempo', methods=['POST'])
def time_watch():
    id = int(session['id'])
    video = int(request.form['video'])
    
    f = film_user.search(video, id)
    if f:
        return jsonify({'time': f.time})
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
