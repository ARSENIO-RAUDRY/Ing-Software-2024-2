from flask import Blueprint, request, render_template, flash, url_for
from alchemyClasses.Usuarios import Usuarios
from alchemyClasses.Peliculas import Peliculas
from alchemyClasses.Rentar import Rentar
from alchemyClasses import db

renta_blueprint = Blueprint('renta', __name__, url_prefix='/renta')

@renta_blueprint.route('/')
def ver_rentas():
    rentas = Rentar.query.all()
    return render_template('rentas.html', rentas=rentas)

@renta_blueprint.route('/agregar', methods=['GET','POST'])
def agregar_renta():
    if request.method == 'GET':
        return render_template('crear_renta.html')
    else:
        idUsuario = request.form['idUsuario']
        idPelicula = request.form['idPelicula']
        fecha_renta = request.form['fecha_renta']
        dias_de_renta = request.form['dias_de_renta']
        estatus = 1 if request.form.get('estatus') else 0

        if not idUsuario or not idPelicula or not fecha_renta or not dias_de_renta or not estatus:
            flash('Campos incompletos', 'error')
            return redirect(url_for('renta.agregar_renta'))

        if not Usuarios.query.filter_by(idUsuario=idUsuario).first():
            flash('Usuario no existente', 'error')
            return redirect(url_for('renta.agregar_renta'))

        if not Peliculas.query.filter_by(idPelicula=idPelicula).first():
            flash('Pelicula no existente', 'error')
            return redirect(url_for('renta.agregar_renta'))
        
        nueva_renta = Rentar(idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus)
        db.session.add(nueva_renta)
        db.session.commit()
        flash('Renta creado', 'success')
        return redirect(url_for('renta.ver_rentas'))


@renta_blueprint.route('/modificar', methods=['GET','POST'])
def modificar_renta():
    if request.method == 'POST':
        id_renta = request.form.get('id_renta')
        return redirect(url_for('renta.modificar_renta_id', id=id_renta))

    return render_template('ingresa_id_renta.html')

@renta_blueprint.route('/modificar/<int:id>', methods=['GET, POST'])
def modificar_renta_id(id):
    renta = Renta.query.get.id(id)

    if not renta:
        flash('Renta no encontrado o ID invalido', 'error')
        return render_template('ingresa_id_renta')

    if request.method == 'GET':
        return render_template('modificar_renta.html', renta=renta)

    elif request.method == 'POST':

        renta.estatus = 1 if request.form.get('estatus') else 0
        db.session.commit()
        flash('Estatus de renta modificada :D', 'success')
        return redirect(url_for('renta.ver_rentas'))
