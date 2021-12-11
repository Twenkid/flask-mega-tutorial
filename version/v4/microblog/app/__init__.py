#v.0.4
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models

db.create_all()

''' v0.3
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes

'''