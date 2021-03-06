from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from GymHome.models import User

class LoginForm(FlaskForm):
    userid = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    remember_me = BooleanField('Recordarme')
    submit = SubmitField('Iniciar sección')


class dataForm(FlaskForm):
    dato = StringField('Dato')
    ejercicio = StringField('Ejercicio')
    nombree = StringField('nombree')
    op = StringField('op')
    submit = SubmitField('Iniciar sección')

class ComprarForm(FlaskForm):
    fecha = StringField('fecha', validators=[DataRequired()])
    hora = StringField('hora', validators=[DataRequired()]) 
    direccion = StringField('direccion', validators=[DataRequired()]) 
    telefono = StringField('telefono', validators=[DataRequired()]) 
    submit = SubmitField('Iniciar sección')

class RutinaForm(FlaskForm):
    tipoEjercicio = StringField('tipoejErcicio', validators=[DataRequired()])
    semana = StringField('Semana', validators=[DataRequired()])
    series = StringField('Series', validators=[DataRequired()])
    repeticiones = StringField('Repeticiones', validators=[DataRequired()])
    peso = StringField('Peso', validators=[DataRequired()])
    descanso = StringField('Descanso', validators=[DataRequired()])   
    submit = SubmitField('Iniciar sección')

class RegistrationForm(FlaskForm):
    userid=StringField('Usuario', validators=[DataRequired()])
    username = StringField('Nombre', validators=[DataRequired()])
    usersurname = StringField('Apellido', validators=[DataRequired()])
    edad = StringField('Edad', validators=[DataRequired()])
    gender = StringField('Genero', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    password2 = PasswordField(
        'Repetir Contraseña', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrar')

    def Validar_userid(self, username):
        user = User.query.filter_by(userid=userid.data).first()
        if user is not None:
            raise ValidationError('Por favor ingrese un usuario diferente.')

    def Validar_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Por favor ingrese un email diferente.')