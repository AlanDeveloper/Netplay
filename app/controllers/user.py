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

        session['id'] = resp.id
        session['name'] = name
        session['email'] = email
        session['password'] = password
        session['admin'] = False

        return redirect('/filme/lista')
    else:
        return render_template('user/register.html')

@user_bp.route('/entrar', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        u = user.search(email, password)
        if u:
            session['id'] = u.id
            session['name'] = u.name
            session['email'] = u.email
            session['password'] = request.form['password']
            session['admin'] = u.typeAdmin
            return redirect('/filme/lista')
        else: 
            error = 'Dados incorretos'
            return render_template('user/login.html', error=error)
    else:
        return render_template('user/login.html')        
      
@user_bp.route('/sair', methods=['GET', 'POST'])
def exit():
    session.clear()
    return redirect('/')

@user_bp.route('/excluir', methods=['GET', 'POST'])
def delete():
    email = session['email']
    password = request.form['password']
    u = user.search(email, password)
    if u:
        user.delete(u.id)
        return redirect('/usuario/sair')
    else:
        error = 'Senha incorreta'
        ls = user.search(session['email'], password)

    return render_template('/user/update.html', ls=ls, error = error)


@user_bp.route('/atualizar', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        newpassword = request.form['newpassword']
        
        if session['password'] == password:
            if len(newpassword) == 0:
                newpassword = session['password']

            u = user.search(session['email'], password)
            if u:
                resp = user(name, email, newpassword)
                resp.id = u.id
                resp.typeAdmin = u.typeAdmin
                user.update(resp)

                session['name'] = name
                session['email'] = email
                session['password'] = newpassword
                return redirect('/filme/lista')
        else:
            ls = user.search(session['email'], session['password'])
            error = 'Senha incorreta'
            return render_template('user/update.html', error=error, ls=ls)
            
    else:
        ls = user.search(session['email'], session['password'])
        return render_template('user/update.html', ls=ls)

def search(email, password):
    u = user.search(email, password)

    return u
