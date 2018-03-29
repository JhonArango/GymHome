from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from GymHome import db
from flask_login import UserMixin
from GymHome import login

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    usersurname = db.Column(db.String(64), index=True, unique=True)
    edad = db.Column(db.Integer, index=True, unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)  

    def ingresar_contraseña(self, password):
        self.password_hash = generate_password_hash(password)

    def verificar_contraseña(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))