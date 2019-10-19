#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from app import app
from flask import Blueprint, render_template, request, redirect, flash, Flask, url_for
from app.controllers.control import control
from app.controllers.film import film_bp

from app.models.film import film

from flask_sqlalchemy import SQLAlchemy
from app import db

app.register_blueprint(control)
app.register_blueprint(film_bp)

@app.before_first_request
def before():
    db.create_all()

@app.route('/drop')
def drop():
    db.drop_all()

@app.route('/')
def index():
    return redirect(control.url_prefix)
