# -*- coding: utf-8 -*-
from flask import render_template, request,redirect
from flask import Blueprint, flash, Flask
from app.models import __init__
#from app.models.daoTemporada import TemporadaDAO
#from app.models.daoSerie import SerieDAO
#from app.models.serie import Serie
#from app.models.temporada import Temporada
#from app.models.dao import UsuarioDAO

from app import db

control = Blueprint('control', __name__, url_prefix='/')

@control.route('/')
def index():
    return render_template('printer/index.html')

@control.route('/home')
def home():
    return render_template('printer/home.html')
