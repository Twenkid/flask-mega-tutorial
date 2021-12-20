#v.0.14
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging  #errors ... v7
from logging.handlers import SMTPHandler
from logging.handlers import RotatingFileHandler
import os
from flask_mail import Mail #v10
from flask_bootstrap import Bootstrap #v11 BS 3
from flask_moment import Moment #v12
from flask_babel import Babel #v13 - too much work, but not critical - skip; localisation etc.
#v14 microsoft translation - free but requires a card registration
from flask_babel import Babel, lazy_gettext as _l #v13
from flask import request #v14

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

db.create_all()
                         
login = LoginManager(app)
login.login_view = 'login'

mail = Mail(app) #v10
bootstrap = Bootstrap(app) #v11  #bootstrap/base.html
moment = Moment(app)    
babel = Babel(app)

#@babel.localeselector
#def get_locale():
#    return request.accept_languages.best_match(app.config['LANGUAGES'])   

if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.DEBUG) #     INFO) #DEBUG, INFO, WARNING, ERROR and CRITICAL
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)    
    app.logger.info('Microblog startup')

#@babel.localeselector
#def get_locale():
#    return request.accept_languages.best_match(app.config['LANGUAGES'])
    
@babel.localeselector
def get_locale():
    # return request.accept_languages.best_match(app.config['LANGUAGES'])
    return 'es'
    
from app import routes, models, errors #at the end



''' v0.3
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes

'''