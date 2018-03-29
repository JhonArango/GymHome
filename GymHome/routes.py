from flask import render_template,flash,redirect,url_for,request
from GymHome import GymHome,db
from GymHome.forms import LoginForm,RegistrationForm
from flask_login import current_user, login_user,logout_user,login_required
from GymHome.models import User
from werkzeug.urls import url_parse

@GymHome.route('/')
@GymHome.route('/index')
def index():
    posts = [
        {
            'indice': 'Uso',
            'body': 'Si desea conocer como funciona GymHome  dar click a ayuda'
        },
        {
            'indice': 'Propiedades',
            'body': 'Si desea saber acerca de la configuracion dar click a Propiedades'
        },
        {
        	'indice': 'login',
            'body': 'Si desea ingresar a la app dar click a login'
        }
    ]
    return render_template('index.html', title='Home',posts=posts)

@GymHome.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.verificar_contraseña(form.password.data):
            flash('Usuario invalido o contraseña incorrecta')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Inicio Seccion', form=form)

@GymHome.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,usersurname=form.usersurname.data,edad=form.edad.data, email=form.email.data)
        user.ingresar_contraseña(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Felicitaciones,Tu registro ha sido exitoso!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Registrar', form=form)

@GymHome.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))