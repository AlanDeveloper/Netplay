#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from app import app
from flask import Blueprint, render_template, request, redirect, flash, Flask, url_for
from app.controllers.control import control
from app.controllers.film import film_bp

#from app.controllers.usuario import usuario
#from app.controllers.temporada import temporada
#from app.controllers.serie import serie

from app.models.film import film

from flask_sqlalchemy import SQLAlchemy
from app import db

app.register_blueprint(control)
app.register_blueprint(film_bp)

@app.before_first_request
def before():
    db.create_all()

@app.route('/')
def index():
    return redirect(control.url_prefix)
