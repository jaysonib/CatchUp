import warnings
from datetime import timedelta

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

app = Flask(__name__)

app.secret_key = 'sessionData'

app.config['TESTING'] = True

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['SQLALCHEMY_ECHO'] = True

app.config['SQLALCHEMY_RECORD_QUERIES'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/catchup'

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=25)

#app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0

app.config['DEBUG'] = True

db = SQLAlchemy(app)

import project.com.controller
