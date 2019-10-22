# -*- coding: utf-8 -*-
from flask import render_template, request, redirect
from flask import Blueprint, flash, Flask, session
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

        session['name'] = name
        session['admin'] = resp.typeAdmin

        return redirect('/')
    else:
        return render_template('user/create.html')

@user_bp.route('/entrar', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        u = user.search(email, password)
        if u:
            session['name'] = u.name
            session['admin'] = u.typeAdmin

            return redirect('/')
        else: 
            error = 'Dados incorretos'
            return render_template('user/create.html', error=error)
    else:
        return render_template('user/create.html')        
      
@user_bp.route('/sair', methods=['GET', 'POST'])
def exit():
    session['name'] = None
    session['admin'] = False

    return redirect('/')

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
