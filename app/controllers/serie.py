# -*- coding: utf-8 -*-
from random import choice
import os
from time import gmtime, strftime
from werkzeug.utils import secure_filename
from flask import Blueprint, Flask, render_template, request, redirect, session, jsonify
from app.models.serie import serie
from app.models.episode import episode
from app.models import __init__

from sqlalchemy import exc

from app import path

serie_bp = Blueprint('serie', __name__, url_prefix='/serie')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'mp4'])


@serie_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        synopsis = request.form['synopsis']
        ageRange = request.form['ageRange']
        season = request.form['season']
        file = request.files['file']

        try:
            checkbox = request.form.getlist('checkbox')
            genero = ';'.join(checkbox)+';'

            if title != '' and synopsis != '' and ageRange != '':
                newname = upload(file, 'images')
            resp = serie(title, synopsis, ageRange, genero, season, newname)
            serie.add(resp)

            return redirect('/serie/lista')
        except UnboundLocalError:
            error = 'Todos os campos devem ser preenchidos!'
            return render_template('serie/create.html', error=error)
        except exc.IntegrityError:
            error = 'Título já cadastrado!'
            return render_template('serie/create.html', error=error)

    else:
        return render_template('serie/create.html')

@serie_bp.route('/del/<id>', methods=['GET', 'POST'])
def delete(id):
    file = serie.search(id)
    os.remove(path.format('serie', 'images') + file.image)
    file = episode.search_all(id)
    for item in file:
        os.remove(path.format('serie', 'videos') + item.video)
    serie.delete(id)
    return redirect('/serie/lista')

@serie_bp.route('/atualizar/<id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        title = request.form['title']
        synopsis = request.form['synopsis']
        ageRange = request.form['ageRange']
        season = request.form['season']
        file = request.files['file']
        checkbox = request.form.getlist('select')
        genero = ';'.join(checkbox)+';'
        resp = serie.search(id)

        if file:
            newname = upload(file, 'images')

            os.remove(path.format('serie', 'images') + resp.image)
            resp = serie(title, synopsis, ageRange, genero, season, newname)
        else:
            resp = serie(title, synopsis, ageRange, genero, season)
        resp.id = id

        serie.update(resp)
        return redirect('/serie/lista')
    else:
        ls = serie.search(id)
        return render_template('serie/update.html', ls=ls)

@serie_bp.route('/lista', methods=['GET', 'POST'])
def list():
    ls = serie.ls()
    return render_template('serie/list.html', ls=ls)

@serie_bp.route('/lista/<serie_id>', methods=['GET', 'POST'])
def list_season(serie_id):
    ls = serie.search(serie_id)
    return render_template('serie/list_season.html', ls=ls)

@serie_bp.route('/lista/<serie_id>/<season_id>', methods=['GET', 'POST'])
def list_episode(serie_id, season_id):
    ls = episode.search(serie_id, season_id)
    v= []

    for item in ls:
        v.append({
            'id': item.id,
            'title': item.title,
            'episode_number': item.episode_number,
            'video': item.video
        })
    
    return jsonify(v)

@serie_bp.route('/<serie_id>/<season_id>/<episode_id>', methods=['GET', 'POST'])
def watch_episode(serie_id, season_id, episode_id):
    ls = episode.search_episode(serie_id, season_id, episode_id)
    s = serie.search(serie_id)
    return render_template('serie/info.html',serie=s, ls=ls)

@serie_bp.route('/episodio', methods=['GET', 'POST'])
def register_episode():

    if request.method == 'POST':
        title = request.form['title']
        serie_id = request.form['serieId']
        season_number = request.form['seasonNumber']
        video = request.files['video']
        newname = upload(video, 'videos')
        episode_number = len(episode.search(serie_id, season_number))

        try:

            p = episode(title, serie_id, season_number, episode_number, newname)
            episode.add(p)
    
            return redirect('/serie/lista')
        except UnboundLocalError:
            ls = serie.ls()
            error = 'Todos os campos devem ser preenchidos!'
            return render_template('serie/create_episode.html', error=error, ls=ls)
        except exc.IntegrityError:
            ls = serie.ls()
            error = 'Título já cadastrado!'
            return render_template('serie/create_episode.html', error=error, ls=ls)

    else:
        ls = serie.ls()
        return render_template('serie/create_episode.html', ls=ls)

def upload(file, folder):
    dt = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(path.format('serie', folder), filename))
        newname = dt.replace(' ', '-').replace(':', '-') + \
            '_' + generate(15) + '.' + filename.split('.')[1]
        os.rename(
            path.format('serie', folder) + filename,
            path.format('serie', folder) + newname
        )
    return newname

def generate(n):
    caracters = '0123456789abcdefghijlmnopqrstuwvxz'
    string = ''
    for char in range(n):
            string += choice(caracters)
    return string

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@serie_bp.route('/temporada', methods=['GET', 'POST'])
def get_season():
    id = int(request.form['id'])

    s = serie.search(id)

    return jsonify({'season': s.season})
