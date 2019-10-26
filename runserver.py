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
    u = user.search('admin@gmail.com', 'admin')
    
    if not u:
        u = user('admin', 'admin@gmail.com', 'admin')
        u.typeAdmin = True
        user.add(u)

    db.create_all()

@app.route('/drop')
def drop():
    db.drop_all()

@app.route('/')
def index():
    return redirect(control.url_prefix)
