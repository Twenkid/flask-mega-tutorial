#v.0.4
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

db.create_all()

login = LoginManager(app)
login.login_view = 'login'

from app import routes, models #at the end

''' v0.3
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes

'''