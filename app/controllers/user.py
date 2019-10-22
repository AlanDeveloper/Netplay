# -*- coding: utf-8 -*-
from flask import render_template, request, redirect
from flask import Blueprint, flash, Flask
from app.models import __init__
from app.models.user import user

user_bp = Blueprint('user', __name__, url_prefix='/user')

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
