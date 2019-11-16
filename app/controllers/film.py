# -*- coding: utf-8 -*-
from random import choice
import os
from time import gmtime, strftime
from werkzeug.utils import secure_filename
from flask import Blueprint, Flask, render_template, request, redirect, session
from app.models.film import film
from app.models import __init__

from sqlalchemy import exc

from app import path

film_bp = Blueprint('film', __name__, url_prefix='/filme')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'mp4'])

@film_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        synopsis = request.form['synopsis']
        ageRange = request.form['ageRange']
        file = request.files['file']
        video = request.files['video']
        
        try:
            generos = request.form.getlist('genero')

            v = ''
            for gen in generos:
                v += gen + ';'

            if title != '' and synopsis != '' and ageRange != '':
                newname = upload(file, 'images')
                newname2 = upload(video, 'videos')
            resp = film(title, synopsis, ageRange, v, newname, newname2)
            film.add(resp)

            return redirect('/filme/lista')
        except UnboundLocalError:
            error = 'Todos os campos devem ser preenchidos!' 
            return render_template('film/create.html', error=error)
        except exc.IntegrityError:
            error = 'Título já cadastrado!' 
            return render_template('film/create.html', error=error)
        
    else:
        return render_template('film/create.html')

@film_bp.route('/lista', methods=['GET', 'POST'])
def list():
    ls = film.ls()
    return render_template('film/list.html', ls=ls)

@film_bp.route('/del/<id>', methods=['GET', 'POST'])
def delete(id):
    file = film.search(id)
    os.remove(path.format('film', 'images') + file.image)
    os.remove(path.format('film', 'videos') + file.video)
    film.delete(id)
    return redirect('/filme/lista')

@film_bp.route('/atualizar/<id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        title = request.form['title']
        synopsis = request.form['synopsis']
        ageRange = request.form['ageRange'] 
        file = request.files['file']
        video = request.files['video']

        resp = film.search(id)

        if video and file:
            newname = upload(file, 'images')
            newname2 = upload(video, 'videos')
            
            os.remove(path.format('film', 'images') + resp.image)
            os.remove(path.format('film', 'videos') + resp.video)
            resp = film(title, synopsis, ageRange, newname, newname2)
        elif file:
            newname = upload(file, 'images')

            os.remove(path.format('film', 'images') + resp.image)
            resp = film(title, synopsis, ageRange, newname)
        elif video: 
            newname2 = upload(video, 'videos')
            
            os.remove(path.format('film', 'videos') + resp.video)
            resp = film(title, synopsis, ageRange, None, newname2)
        else:
            resp = film(title, synopsis, ageRange)
        resp.id = id

        film.update(resp)
        return redirect('/filme/lista')
    else:
        ls = film.search(id)
        return render_template('film/update.html', ls=ls)


@film_bp.route('/buscar', methods=['GET', 'POST'])
def search():
    s = request.form['search']
    ls = film.searchName(s)
    return render_template('film/list.html', ls=ls)

def upload(file, folder):
    dt = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(path.format('film', folder), filename))
        newname = dt.replace(' ', '-').replace(':', '-') + '_' + generate(15) + '.' + filename.split('.')[1]
        os.rename(
            path.format('film', folder) + filename,
            path.format('film', folder) + newname
        )
    return newname

@film_bp.route('/info/<id>', methods=['GET', 'POST'])
def info(id):
    ls = film.search(id)
    return render_template('film/info.html', ls=ls)

def generate(n):
    caracters = '0123456789abcdefghijlmnopqrstuwvxz'
    string = ''
    for char in range(n):
        string += choice(caracters)
    return string

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
