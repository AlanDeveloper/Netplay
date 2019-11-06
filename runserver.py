#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from app import app
from flask import Blueprint, render_template, request, redirect, flash, Flask, url_for, session
from app.controllers.control import control
from app.controllers.user import user
from app.controllers.film import film_bp
from app.controllers.user import user_bp

from app.models.user import user

from flask_sqlalchemy import SQLAlchemy
from app import db

app.register_blueprint(control)
app.register_blueprint(film_bp)
app.register_blueprint(user_bp)

@app.before_first_request
def before():
    db.create_all()
    
    u = user.search('admin@gmail.com', 'admin')
    if not u:
        u = user('admin', 'admin@gmail.com', 'admin')
        u.typeAdmin = True
        user.add(u)

@app.route('/create')
def create():
    db.create_all()

@app.route('/drop')
def drop():
    db.drop_all()

@app.before_request
def before_request_func():
    if (request.path != '/' and request.path !='/usuario/entrar' and request.path !='/usuario/') and (not request.path.startswith('/static')):
        if not session:
            return redirect(control.url_prefix)
            
@app.route('/')
def index():
    return redirect(control.url_prefix)
