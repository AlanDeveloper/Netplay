# -*- coding: utf-8 -*-
from flask import Blueprint, Flask, render_template, request, redirect, session, jsonify
from app.models.film_user import film_user
from app.models.film import film
from app.models import __init__

from app import db

control = Blueprint('control', __name__, url_prefix='/')

@control.route('/')
def index():
    return render_template('user/login.html')


@control.route('/home', methods=['GET', 'POST'])
def list_watching():
    items = []
    ls = film_user.searchFilms(session['id'])

    for item in ls:
        f = film.search(item.film_id)
        items.append(f)

    return render_template('printer/home.html', ls=items)

@control.route('/assistidos', methods=['POST'])
def watching():
    id = int(session['id'])
    video = int(request.form['video'])
    time = request.form['time']
    
    f = film_user.search(video, id)
    if f:
        f.time = time
        film_user.update(f)
    else:
        f = film_user(video, id, time)
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

