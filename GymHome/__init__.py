from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail

GymHome = Flask(__name__)
GymHome.config.from_object(Config)
db = SQLAlchemy(GymHome)
mail = Mail(GymHome)
migrate = Migrate(GymHome, db)
login = LoginManager(GymHome)
login.login_view = 'login'


from GymHome import routes,models