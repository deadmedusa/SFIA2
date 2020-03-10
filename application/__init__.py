from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import getenv

app = Flask(__name__)

app.config['SECRET_KEY'] = getenv('DINER_SECRET_KEY')

app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DINER_DB_URI'))
db = SQLAlchemy(app)

from application import routes
