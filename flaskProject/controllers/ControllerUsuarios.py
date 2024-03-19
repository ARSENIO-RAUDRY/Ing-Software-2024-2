from flask import Blueprint, request, render_template, flash, url_for
from random import randint
from alchemyClasses.Usuarios import Usuarios
from alchemyClasses.Rentar import Rentar
from alchemyClasses import db

usuario_blueprint = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario_blueprint.route('/')
def ver_usuarios():
    usuarios = Usuarios.query.all()
    return render_template('usuarios.html', usuarios=usuarios)

@usuario_blueprint.route('/agregar', methods=['GET','POST'])
def agregar_usuario():
    if request.method == 'GET':
        return render_template('crear_usuario.html')
    else:
        nombre = request.form['nombre']
        apPat = request.form['apPat']
        apMat = request.form['apMat']
        password = request.form['password']
        email = request.form['email']
        superUser = True if request.form.get('superUser') else False

        if not nombre or not apPat or not apMat or not password or not email:
            flash('Campos incompletos', 'error')
            return redirect(url_for('usuario.agregar_usuario'))

        if Usuarios.query.filter_by(email=email).first():
            flash('Email ya registrado', 'error')
            return redirect(url_for('usuario.agregar_usuario'))
        
        nuevo_usuario = Usuarios(nombre, apPat, apMat, password, email, superUser)
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash('Usuario creado', 'success')
        return redirect(url_for('usuario.ver_usuarios'))


@usuario_blueprint.route('/modificar', methods=['GET','POST'])
def modificar_usuario():
    if request.method == 'POST':
        id_usuario = request.form.get('id_usuario')
        return redirect(url_for('usuario.modificar_usuario_id', id=id_usuario))

    return render_template('ingresa_id_usuario.html')

@usuario_blueprint.route('/modificar/<int:id>', methods=['GET, POST'])
def modificar_usuario_id(id):
    usuario = Usuario.query.get.id(id)

    if not usuario:
        flash('Usuario no encontrado o ID invalido', 'error')
        return render_template('ingresa_id_usuario')

    if request.method == 'GET':
        return render_template('modificar_usuario.html', usuario=usuario)

    elif request.method == 'POST':

        usuario.nombre = request.form.get['nombre']
        usuario.apPat = request.form.get['apPat']
        usuario.apMat = request.form.get['apMat']
        usuario.password = request.form.get['password']
        usuario.email = request.form['email']
        usuario.superUser = True if request.form.get('superUser') else False

        if not usuario.nombre or not usuario.apPat or not usuario.apMat or not usuario.password or not email:
            flash('Campos incompletos', 'error')
            return render_template('modificar_usuario.html', usuario=usuario)
        
        if Usuarios.query.filter((Usuarios.email == usuario.email) & (Usuarios.idUsuario != id)).first():
            flash('Correo ya existente','error')
            return render_template('modificar_usuario.html', usuario=usuario)

        db.session.commit()
        flash('Usuario modificado :D', 'success')
        return redirect(url_for('usuario.ver_usuarios'))

@usuario_blueprint.route('/modificar', methods=['GET','POST'])
def eliminar_usuario():
    if request.method == 'POST':
        id_usuario = request.form.get('id_usuario')
        return redirect(url_for('usuario.eliminar_usuario_id', id=id_usuario))

    return render_template('ingresa_id_usuario.html')


@usuario_blueprint.route('/eliminar/<int:id>', methods=['GET','POST'])
def eliminar_usuario_id(id):
    usuario = Usuario.query.get.id(id)

    if not usuario:
        flash('Usuario no encontrado o ID invalido', 'error')
        return render_template('ingresa_id_usuario')

    else:
        rentas_asociadas = Rentar.query.filter_by(idUsuario=id).first()

        if not rentas_asociadas:
            db.session.delete(usuario)
            db.session.commit()
            flash('Usuario eliminado', 'success')
            return redirect(url_for('usuario.ver_usuarios'))
        else:
            flash('El usuario tiene rentas asociadas, elimine estas primero', 'error')
            return redirect(url_for('usuario.ver_usuarios'))
