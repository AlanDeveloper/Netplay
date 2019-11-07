# -*- coding: utf-8 -*-
# __version__ = '0.1'
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask('app')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'secret')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/netplay'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Bootstrap(app)