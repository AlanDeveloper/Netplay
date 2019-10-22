# -*- coding: utf-8 -*-
from flask import render_template, request, redirect
from flask import Blueprint, flash, Flask
from app.models import __init__

#from app.models.daoTemporada import TemporadaDAO
#from app.models.daoSerie import SerieDAO
#from app.models.serie import Serie
from app.models.usuario import Usuario
#from app.models.dao import UsuarioDAO



usuario = Blueprint('usuario', __name__, url_prefix='/')

@usuario.route('/cadastrar',methods=['GET','POST'])
def cadastrar():
    user = Usuario()
    if(request.method == "POST"):
        user.nome = request.form['nome']
        user.email = request.form['email'] 
        user.tipo = False            
        user.senha = request.form['senha']
        db.session.add(user)
        db.session.commit()
        return "enviado"
    else:
        user.nome = request.form['nome']
        user.email = request.form['email']        
        user.senha = request.form['senha']
        return user.nome
