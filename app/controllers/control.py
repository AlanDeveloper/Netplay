# -*- coding: utf-8 -*-
from flask import render_template, request,redirect, session, jsonify
from flask import Blueprint, flash, Flask
from app.models import __init__
from app.models.film_user import film_user

from app import db

control = Blueprint('control', __name__, url_prefix='/')

@control.route('/')
def index():
    return render_template('printer/index.html')

@control.route('/home')
def home():
    return render_template('printer/home.html')

@control.route('/watch', methods=['POST'])
def watch():
    video = request.form['video']
    time = request.form['time']
    id = session['id']
    
    f = film_user(int(video), int(id), int(time))
    film_user.add(f)
