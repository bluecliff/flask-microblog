from flask import Flask
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate
import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir, ADMINS,MAIL_SERVER,MAIL_USERNAME,MIAL_PORT,MAIL_PASSWORD

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

if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    credentials = None
    if MAIL_USERNAME or MAIL_PASSWORD:
        credentials=(MAIL_USERNAME,MAIL_PASSWORD)
    mail_handler = SMTPHandler((MAIL_SERVER,MIAL_PORT),'noreply@'+MAIL_SERVER,ADMINS,'microblog failure',credentials)
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)
if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('tmp/microblog.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('microblog startup')
#import sys
#print sys.path
from app import views,models
