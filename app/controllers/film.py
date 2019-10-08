# -*- coding: utf-8 -*-
from flask import render_template, request, redirect
from flask import Blueprint, flash, Flask
from app.models import __init__
from app.models.film import film
#from app.models.daoTemporada import TemporadaDAO
#from app.models.daoSerie import SerieDAO
#from app.models.serie import Serie
#from app.models.temporada import Temporada
#from app.models.dao import UsuarioDAO

from app import db

film_bp = Blueprint('film', __name__, url_prefix='/filme')

@film_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        synopsis = request.form['synopsis']
        ageRange = request.form['ageRange']
        resp = film(title, synopsis, ageRange)

        film.add(resp)
        return redirect('/')
    else:
        return render_template('film/create.html')
