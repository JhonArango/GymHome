from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from GymHome import db
from flask_login import UserMixin
from GymHome import login

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid=db.Column(db.String(64), index=True, unique=True)
    username = db.Column(db.String(64), index=True)
    usersurname = db.Column(db.String(64), index=True)
    edad = db.Column(db.Integer, index=True)
    Peso = db.Column(db.Integer, index=True)
    Altura = db.Column(db.Integer, index=True)
    gender = db.Column(db.String(64), index=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), index=True, unique=True)
    ejPecho=db.relationship('Pecho', backref='RutinaPe' , lazy='dynamic')
    ejHombro=db.relationship('Hombro', backref='RutinaHo' , lazy='dynamic')
    ejBiceps=db.relationship('Biceps', backref='RutinaBi' , lazy='dynamic')
    ejTriceps=db.relationship('Triceps', backref='RutinaTr' , lazy='dynamic')
    ejCuadriceps=db.relationship('Cuadriceps', backref='RutinaCu' , lazy='dynamic')
    ejFemoral=db.relationship('Femoral', backref='RutinaFe' , lazy='dynamic')
    ejPantorrilla=db.relationship('Pantorrilla', backref='RutinaPa' , lazy='dynamic')
    def __repr__(self):
        return '<User {}>'.format(self.username)  

    def ingresar_contraseña(self, password):
        self.password_hash = generate_password_hash(password)

    def verificar_contraseña(self, password):
        return check_password_hash(self.password_hash, password)

class Pecho(db.Model):
    idPe = db.Column(db.Integer, primary_key=True)
    nombreEjer = db.Column(db.String(64), index=True)
    semana = db.Column(db.Integer, index=True)
    series = db.Column(db.Integer, index=True)
    repeticiones = db.Column(db.Integer, index=True)
    peso = db.Column(db.Integer, index=True, unique=True)
    descanso = db.Column(db.Integer, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Hombro(db.Model):
    idHo = db.Column(db.Integer, primary_key=True)
    nombreEjer = db.Column(db.String(64), index=True)
    semana = db.Column(db.Integer, index=True)
    series = db.Column(db.Integer, index=True)
    repeticiones = db.Column(db.Integer, index=True)
    peso = db.Column(db.Integer, index=True)
    descanso = db.Column(db.Integer, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Biceps(db.Model):
    idBi = db.Column(db.Integer, primary_key=True)
    nombreEjer = db.Column(db.String(64), index=True)
    semana = db.Column(db.Integer, index=True)
    series = db.Column(db.Integer, index=True)
    repeticiones = db.Column(db.Integer, index=True)
    peso = db.Column(db.Integer, index=True)
    descanso = db.Column(db.Integer, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 

class Triceps(db.Model):
    idTr = db.Column(db.Integer, primary_key=True)
    nombreEjer = db.Column(db.String(64), index=True)
    semana = db.Column(db.Integer, index=True)
    series = db.Column(db.Integer, index=True)
    repeticiones = db.Column(db.Integer, index=True)
    peso = db.Column(db.Integer, index=True)
    descanso = db.Column(db.Integer, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Cuadriceps(db.Model):
    idCu = db.Column(db.Integer, primary_key=True)
    nombreEjer = db.Column(db.String(64), index=True)
    semana = db.Column(db.Integer, index=True)
    series = db.Column(db.Integer, index=True)
    repeticiones = db.Column(db.Integer, index=True)
    peso = db.Column(db.Integer, index=True)
    descanso = db.Column(db.Integer, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Femoral(db.Model):
    idFe = db.Column(db.Integer, primary_key=True)
    nombreEjer = db.Column(db.String(64), index=True)
    semana = db.Column(db.Integer, index=True)
    series = db.Column(db.Integer, index=True)
    repeticiones = db.Column(db.Integer, index=True)
    peso = db.Column(db.Integer, index=True)
    descanso = db.Column(db.Integer, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  

class Pantorrilla(db.Model):
    idPa = db.Column(db.Integer, primary_key=True)
    nombreEjer = db.Column(db.String(64), index=True)
    semana = db.Column(db.Integer, index=True)
    series = db.Column(db.Integer, index=True)
    repeticiones = db.Column(db.Integer, index=True)
    peso = db.Column(db.Integer, index=True)
    descanso = db.Column(db.Integer, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 



@login.user_loader
def load_user(id):
    return User.query.get(int(id))