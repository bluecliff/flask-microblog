from flask import Flask
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate

app = Flask(__name__)

app.config.from_object('config')
db = SQLAlchemy()
db.app = app
db.init_app(app)

migrate = Migrate(app,db)
manager = Manager(app)
#import sys
#print sys.path
from app import views,models