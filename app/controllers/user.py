# -*- coding: utf-8 -*-
from flask import render_template, request, redirect
from flask import Blueprint, flash, Flask
from app.models import __init__
from app.models.user import user

user_bp = Blueprint('user', __name__, url_prefix='/usuario')

@user_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        resp = user(name, email, password)
        user.add(resp)
        return redirect('/')
    else:
        return render_template('user/create.html')

@user_bp.route('/entrar', methods=['GET', 'POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    if user.search(email, password):
        return redirect('/')
    else: 
        return 'Dados incorretos'

@user_bp.route('/lista', methods=['GET', 'POST'])
def list():
    ls = user.ls()
    return render_template('user/list.html', ls=ls)

@user_bp.route('/del/<id>', methods=['GET', 'POST'])
def delete(id):
    user.delete(id)
    return redirect('/usuario/lista')

@user_bp.route('/atualizar/<id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        resp = user(name, email, password)
        resp.id = id

        user.update(resp)
        return redirect('/usuario/lista')
    else:
        ls = user.search(id)
        return render_template('user/update.html', ls=ls)
