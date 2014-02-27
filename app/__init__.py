from flask import Flask
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)
app.config.from_object('config')

from app import views