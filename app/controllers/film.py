# -*- coding: utf-8 -*-
import os
from time import gmtime, strftime
from werkzeug.utils import secure_filename
from flask import render_template, request, redirect, session
from flask import Blueprint, flash, Flask
from app.models import __init__
from app.models.film import film

path = r"C:\\Users\usuar\Documents\GitHub\Netplay\app\static\\{}\\"

from app import db

film_bp = Blueprint('film', __name__, url_prefix='/filme')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'mp4'])

@film_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        duration = request.form['duration']
        synopsis = request.form['synopsis']
        ageRange = request.form['ageRange']
        file = request.files['file']
        video = request.files['video']
        
        try:
            if title != '' and duration != '' and synopsis != '' and ageRange != '':
                newname = upload(file, 'images')
                newname2 = upload(video, 'videos')

            resp = film(title, duration, synopsis, ageRange, newname, newname2)
            film.add(resp)
            return redirect('/filme/lista')
        except UnboundLocalError:
            error = 'Todos os campos devem ser preenchidos!' 
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
    os.remove(path.format('images') + file.image)
    os.remove(path.format('videos') + file.video)
    film.delete(id)
    return redirect('/filme/lista')

@film_bp.route('/atualizar/<id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        title = request.form['title']
        duration = request.form['duration']
        synopsis = request.form['synopsis']
        ageRange = request.form['ageRange'] 
        file = request.files['file']
        video = request.files['video']

        resp = film.search(id)

        if video and file:
            newname = upload(file, 'images')
            newname2 = upload(video, 'videos')
            
            os.remove(path.format('images') + resp.image)
            os.remove(path.format('videos') + resp.video)
            resp = film(title, duration, synopsis, ageRange, newname, newname2)
        elif file:
            newname = upload(file, 'images')

            os.remove(path.format('images') + resp.image)
            resp = film(title, duration, synopsis, ageRange, newname)
        elif video: 
            newname2 = upload(video, 'videos')
            
            os.remove(path.format('videos') + resp.video)
            resp = film(title, duration, synopsis, ageRange, None, newname2)
        else:
            resp = film(title, duration, synopsis, ageRange)
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
        file.save(os.path.join(path.format(folder), filename))
        newname = dt.replace(' ', '-').replace(':', '-') + '.' + filename.split('.')[1]
        os.rename(
            path.format(folder) + filename,
            path.format(folder) + newname
        )
    return newname

@film_bp.route('/info/<id>', methods=['GET', 'POST'])
def info(id):
        ls = film.search(id)
        return render_template('film/info.html', ls=ls)

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
