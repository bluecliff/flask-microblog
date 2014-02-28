from flask import Flask
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate
import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy()
db.app = app
db.init_app(app)

migrate = Migrate(app,db)
manager = Manager(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view='login'
oid = OpenID(app,os.path.join(basedir,'tmp'))

#import sys
#print sys.path
from app import views,models