from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_socketio import SocketIO,send
Lista_foro=[]

GymHome = Flask(__name__)
GymHome.config.from_object(Config)
db = SQLAlchemy(GymHome)
mail = Mail(GymHome)
socketio = SocketIO(GymHome)
migrate = Migrate(GymHome, db)
login = LoginManager(GymHome)
login.login_view = 'login'

from GymHome import routes,models


socketio.run(GymHome,debug=True)

