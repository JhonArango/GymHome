from flask import render_template,flash,redirect,url_for,request
from GymHome import GymHome,db,mail,socketio
from flask_socketio import SocketIO,send
from GymHome.forms import LoginForm,RegistrationForm,RutinaForm,dataForm
from flask_login import current_user, login_user,logout_user,login_required
from GymHome.models import User,load_user,Pecho,Biceps,Triceps,Cuadriceps,Femoral,Pantorrilla,Hombro
from werkzeug.urls import url_parse

@GymHome.route('/')
@GymHome.route('/index')
def index():
    return render_template('index.html', title='Home')

@GymHome.route('/foro')
def foro():
    return render_template('foro.html', title='menu')

@socketio.on('message')
def handlemessage(msg):
    print("mensaje: " + msg)
    u = User.query.filter_by(username=current_user.username).first()

    msg=u.username + ":" + msg
    send(msg,broadcast=True)

@GymHome.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(userid=form.userid.data).first()
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
        u = User.query.filter_by(username=current_user.username).first()
        j = form.tipoEjercicio.data
        l = (j[0]+j[1])
        p = len(j)
        aux = j[p-1]
        print(aux)
        print(l)
        if(l == 'Pe'):
            if(aux == '1'):
                nombre='Barbell Bench Press-Medium Grip'
            if(aux == '2'):
                nombre='Barbell Incline Bench Press Medium-Grip'
            if(aux == '3'):
                nombre='Decline Barbell Bench Press'
            print(nombre)
            r = Pecho(nombreEjer=nombre,semana=form.semana.data,series=form.series.data,repeticiones=form.repeticiones.data,peso=form.peso.data,descanso=form.descanso.data,RutinaPe=u)
        if(l == 'Ho'):
            if(aux == '1'):
                nombre='Side Lateral Raise'
            if(aux == '2'):
                nombre='Standing Military Press'
            if(aux == '3'):
                nombre='Barbell Shoulder Press'
            if(aux == '4'):
                nombre='Dumbbell Shoulder Press'
            r = Hombro(nombreEjer=nombre,semana=form.semana.data,series=form.series.data,repeticiones=form.repeticiones.data,peso=form.peso.data,descanso=form.descanso.data,RutinaHo=u)
        if(l == 'Bi'):
            if(aux == '1'):
                nombre='Dumbbell Bicep Curl'
            if(aux == '2'):
                nombre='Seated Dumbbell Curl'
            if(aux == '3'):
                nombre='Standing Biceps Cable Curl'
            if(aux == '4'):
                nombre='EZ-Bar Skullcrusher'
            r = Biceps(nombreEjer=nombre,semana=form.semana.data,series=form.series.data,repeticiones=form.repeticiones.data,peso=form.peso.data,descanso=form.descanso.data,RutinaBi=u)
        if(l == 'Tr'):
            r = Triceps(nombreEjer=nombre,semana=form.semana.data,series=form.series.data,repeticiones=form.repeticiones.data,peso=form.peso.data,descanso=form.descanso.data,RutinaTr=u) 
        if(l == 'Cu'):
            if(aux == '1'):
                nombre='Leg Press'
            if(aux == '2'):
                nombre='Leg Extensions'
            if(aux == '3'):
                nombre='Barbell Squat'
            if(aux == '4'):
                nombre='Single-Leg Press'
            r = Cuadriceps(nombreEjer=nombre,semana=form.semana.data,series=form.series.data,repeticiones=form.repeticiones.data,peso=form.peso.data,descanso=form.descanso.data,RutinaCu=u)
        if(l == 'Fe'):
            if(aux == '1'):
                nombre='Lying Leg Curls'
            if(aux == '2'):
                nombre='Romanian Dead Lift'
            if(aux == '3'):
                nombre='Deadlift'
            r = Femoral(nombreEjer=nombre,semana=form.semana.data,series=form.series.data,repeticiones=form.repeticiones.data,peso=form.peso.data,descanso=form.descanso.data,RutinaFe=u)
        if(l == 'Pantorrilla'):
            if(aux == '1'):
                nombre='Standing Calf Raises'
            if(aux == '2'):
                nombre='Seated Calf Raise'
            r = Pantorrilla(nombreEjer=nombre,semana=form.semana.data,series=form.series.data,repeticiones=form.repeticiones.data,peso=form.peso.data,descanso=form.descanso.data,RutinaPa=u) 
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
    Pe1 = Pecho.query.filter_by(nombreEjer='Barbell Bench Press-Medium Grip',user_id=u.id)
    Pe2 = Pecho.query.filter_by(nombreEjer='Barbell Incline Bench Press Medium-Grip',user_id=u.id)
    Pe3 = Pecho.query.filter_by(nombreEjer='Decline Barbell Bench Press',user_id=u.id)
    Ho1 = Hombro.query.filter_by(nombreEjer='Side Lateral Raise',user_id=u.id)
    Ho2 = Hombro.query.filter_by(nombreEjer='Standing Military Press',user_id=u.id)
    Ho3 = Hombro.query.filter_by(nombreEjer='Barbell Shoulder Press',user_id=u.id)
    Ho4 = Hombro.query.filter_by(nombreEjer='Dumbbell Shoulder Press',user_id=u.id)
    Bi1 = Biceps.query.filter_by(nombreEjer='Dumbbell Bicep Curl',user_id=u.id)
    Bi2 = Biceps.query.filter_by(nombreEjer='Seated Dumbbell Curl',user_id=u.id)
    Bi3 = Biceps.query.filter_by(nombreEjer='Standing Biceps Cable Curl',user_id=u.id)
    Bi4 = Biceps.query.filter_by(nombreEjer='EZ-Bar Skullcrusher',user_id=u.id)
    Cu1 = Cuadriceps.query.filter_by(nombreEjer='Leg Press',user_id=u.id)
    Cu2 = Cuadriceps.query.filter_by(nombreEjer='Leg Extensions',user_id=u.id)
    Cu3 = Cuadriceps.query.filter_by(nombreEjer='Barbell Squat',user_id=u.id)
    Cu4 = Cuadriceps.query.filter_by(nombreEjer='Single-Leg Press',user_id=u.id)
    Fe1 = Femoral.query.filter_by(nombreEjer='Lying Leg Curls',user_id=u.id)
    Fe2 = Femoral.query.filter_by(nombreEjer='Romanian Dead Lift',user_id=u.id)
    Fe3 = Femoral.query.filter_by(nombreEjer='Deadlift',user_id=u.id)
    Pa1 = Pantorrilla.query.filter_by(nombreEjer='Standing Calf Raises',user_id=u.id)
    Pa2 = Pantorrilla.query.filter_by(nombreEjer='Seated Calf Raise',user_id=u.id)
    form = dataForm()
    if form.validate_on_submit():
        u = User.query.filter_by(username=current_user.username).first()
        if(form.ejercicio.data == 'Pecho'):
            s = Pecho.query.filter_by(nombreEjer=form.nombree.data,semana=form.dato.data,user_id=u.id).first()
        if(form.ejercicio.data == 'Hombro'):
            s = Hombro.query.filter_by(nombreEjer=form.nombree.data,semana=form.dato.data,user_id=u.id).first()
        if(form.ejercicio.data == 'Biceps'):
            s = Biceps.query.filter_by(nombreEjer=form.nombree.data,semana=form.dato.data,user_id=u.id).first()
        if(form.ejercicio.data == 'Triceps'):
            s = Triceps.query.filter_by(nombreEjer=form.nombree.data,semana=form.dato.data,user_id=u.id).first()
        if(form.ejercicio.data == 'Cuadriceps'):
            s = Cuadriceps.query.filter_by(nombreEjer=form.nombree.data,semana=form.dato.data,user_id=u.id).first()
        if(form.ejercicio.data == 'Femoral'):
            s = Femoral.query.filter_by(nombreEjer=form.nombree.data,semana=form.dato.data,user_id=u.id).first()
        if(form.ejercicio.data == 'Pantorrilla'):
            s = Pantorrilla.query.filter_by(nombreEjer=form.nombree.data,semana=form.dato.data,user_id=u.id).first()
        return render_template('lista.html', title='lista',sem = form.dato.data , TipoE = form.nombree.data, s=s)
    return render_template('listarRutina.html', title='listarRutina', form=form, Pe1 =Pe1,Pe2=Pe2,Pe3=Pe3,Bi1 =Bi1,Bi2=Bi2,Bi3=Bi3,Bi4 =Bi4,Ho2=Ho2,Ho3=Ho3,Ho1 =Ho1,Ho4=Ho4,Cu1 =Cu1,Cu2=Cu2,Cu3=Cu3,Cu4 =Cu4,Fe1 =Fe1,Fe2=Fe2,Fe3=Fe3,Pa1 =Pa1,Pa2=Pa2)


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

@GymHome.route('/lista')
def lista():
    return render_template('lista.html', title='menu')

@GymHome.route('/solomillo')
def solomillo():
    return render_template('solomillo.html', title='menu')

@GymHome.route('/proteinas')
def proteinas():
    return render_template('proteinas.html', title='menu')

@GymHome.route('/aminoacidos')
def aminoacidos():
    return render_template('aminoacidos.html')


@GymHome.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))