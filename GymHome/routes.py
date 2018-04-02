from flask import render_template,flash,redirect,url_for,request
from GymHome import GymHome,db
from GymHome.forms import LoginForm,RegistrationForm,RutinaForm
from flask_login import current_user, login_user,logout_user,login_required
from GymHome.models import User,load_user,Pecho,Biceps,Triceps,Cuadriceps,Femoral,Pantorrilla,Hombro
from werkzeug.urls import url_parse

@GymHome.route('/')
@GymHome.route('/index')
def index():
    return render_template('index.html', title='Home')

@GymHome.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        print("hola1")
        return redirect(url_for('index'))
    form = LoginForm()
    print("hola2")
    print(form.username.data)

    if form.validate_on_submit():
        print("hola3")
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
    print("hola3")
    if form.validate_on_submit():
        print("holasdsdsd3")
        user = User(userid=form.userid.data,username=form.username.data,usersurname=form.usersurname.data,edad=form.edad.data, email=form.email.data,gender=form.gender.data)
        user.ingresar_contraseña(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Felicitaciones,Tu registro ha sido exitoso!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Registrar', form=form)

@GymHome.route('/agregarRutina', methods=['GET', 'POST'])
def agregarRutina():
    form = RutinaForm()
    if form.validate_on_submit():
        print("holasdsdsd3")
        u = User.query.filter_by(username=current_user.username).first()
        if(form.tipoEjercicio.data == 'Pecho'):
            r = Pecho(semana=form.semana.data,series=form.series.data,repeticiones=form.repeticiones.data,peso=form.peso.data,descanso=form.descanso.data,RutinaPe=u)
        if(form.tipoEjercicio.data == 'Hombro'):
            r = Hombro(semana=form.semana.data,series=form.series.data,repeticiones=form.repeticiones.data,peso=form.peso.data,descanso=form.descanso.data,RutinaHo=u)
        if(form.tipoEjercicio.data == 'Biceps'):
            r = Biceps(semana=form.semana.data,series=form.series.data,repeticiones=form.repeticiones.data,peso=form.peso.data,descanso=form.descanso.data,RutinaBi=u)
        if(form.tipoEjercicio.data == 'Triceps'):
            r = Triceps(semana=form.semana.data,series=form.series.data,repeticiones=form.repeticiones.data,peso=form.peso.data,descanso=form.descanso.data,RutinaTr=u) 
        if(form.tipoEjercicio.data == 'Cuadriceps'):
            r = Cuadriceps(semana=form.semana.data,series=form.series.data,repeticiones=form.repeticiones.data,peso=form.peso.data,descanso=form.descanso.data,RutinaCu=u)
        if(form.tipoEjercicio.data == 'Femoral'):
            r = Femoral(semana=form.semana.data,series=form.series.data,repeticiones=form.repeticiones.data,peso=form.peso.data,descanso=form.descanso.data,RutinaFe=u)
        if(form.tipoEjercicio.data == 'Pantorrilla'):
            r = Pantorrilla(semana=form.semana.data,series=form.series.data,repeticiones=form.repeticiones.data,peso=form.peso.data,descanso=form.descanso.data,RutinaPa=u) 
        db.session.add(r)
        db.session.commit()
        return redirect(url_for('rutina'))
    return render_template('agregarRutina.html', title='Agregar Rutina', form=form)

@GymHome.route('/rutina', methods=['GET', 'POST'])
@login_required 
def rutina():
    return render_template('rutina.html', title='menu')

@GymHome.route('/listarRutina', methods=['GET', 'POST'])
def listarRutina():
    u = User.query.filter_by(username=current_user.username).first()   
    return render_template('listarRutina.html', title='menu',u=u)

@GymHome.route('/ejercicios')
def ejercicios():
    return render_template('ejercicios.html', title='menu')

@GymHome.route('/alimentacion')
def alimentacion():
    return render_template('alimentacion.html', title='menu')

@GymHome.route('/carnes')
def carnes():
    return render_template('carnes.html', title='menu')

@GymHome.route('/creatina')
def creatina():
    return render_template('creatina.html', title='menu')

@GymHome.route('/pre_entrenos')
def pre_entrenos():
    return render_template('pre_entrenos.html', title='menu')

@GymHome.route('/proteina1')
def proteina1():
    return render_template('proteina1.html', title='menu')

@GymHome.route('/proteina2')
def proteina2():
    return render_template('proteina2.html', title='menu')

@GymHome.route('/quemadores')
def quemadores():
    return render_template('quemadores.html', title='menu')

@GymHome.route('/suplementacion')
def suplementacion():
    return render_template('suplementacion.html', title='menu')

@GymHome.route('/variado')
def variado():
    return render_template('variado.html', title='menu')

@GymHome.route('/verduras')
def verduras():
    return render_template('verduras.html', title='menu')


@GymHome.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))