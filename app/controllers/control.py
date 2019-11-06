# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, session, jsonify
from flask import Blueprint, flash, Flask
from app.models import __init__
from app.models.film_user import film_user

from app import db

control = Blueprint('control', __name__, url_prefix='/')

@control.route('/')
def index():
    if session:
        return render_template('printer/home.html')
    else:
        return redirect('/usuario/entrar')

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
    
