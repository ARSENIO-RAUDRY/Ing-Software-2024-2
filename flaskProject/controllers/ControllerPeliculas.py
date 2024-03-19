from flask import Blueprint, request, render_template, flash, url_for
from random import randint
from alchemyClasses.Peliculas import Peliculas
from alchemyClasses.Rentar import Rentar
from alchemyClasses import db

pelicula_blueprint = Blueprint('pelicula', __name__, url_prefix='/pelicula')

@pelicula_blueprint.route('/')
def ver_peliculas():
    peliculas = Peliculas.query.all()
    return render_template('peliculas.html', peliculas=peliculas)

@pelicula_blueprint.route('/agregar', methods=['GET','POST'])
def agregar_pelicula():
    if request.method == 'GET':
        return render_template('crear_pelicula.html')
    else:
        nombre = request.form['nombre']
        genero = request.form['genero']
        duracion = request.form['duracion']
        inventario = request.form['inventario']
       
        if not nombre or not genero or not duracion or not inventario:
            flash('Campos incompletos', 'error')
            return redirect(url_for('pelicula.agregar_pelicula'))
        
        nueva_pelicula = Peliculas(nombre, genero, duracion, inventario)
        db.session.add(nueva_pelicula)
        db.session.commit()
        flash('Pelicula creada', 'success')
        return redirect(url_for('pelicula.ver_peliculas'))


@pelicula_blueprint.route('/modificar', methods=['GET','POST'])
def modificar_pelicula():
    if request.method == 'POST':
        id_pelicula = request.form.get('id_pelicula')
        return redirect(url_for('pelicula.modificar_pelicula_id', id=id_pelicula))

    return render_template('ingresa_id_pelicula.html')

@pelicula_blueprint.route('/modificar/<int:id>', methods=['GET, POST'])
def modificar_pelicula_id(id):
    pelicula = Pelicula.query.get.id(id)

    if not pelicula:
        flash('Pelicula no encontrada o ID invalido', 'error')
        return render_template('ingresa_id_pelicula')

    if request.method == 'GET':
        return render_template('modificar_pelicula.html', pelicula=pelicula)

    elif request.method == 'POST':

        pelicula.nombre = request.form.get['nombre']
        pelicula.genero = request.form.get['genero']
        pelicula.duracion = request.form.get['duracion']
        pelicula.inventario = request.form.get['inventario']

        if not pelicula.nombre or not pelicula.genero or not pelicula.duracion or not pelicula.inventario:
            flash('Campos incompletos', 'error')
            return render_template('modificar_pelicula.html', pelicula=pelicula)        

        db.session.commit()
        flash('Pelicula modificada :D', 'success')
        return redirect(url_for('pelicula.ver_peliculas'))

@pelicula_blueprint.route('/modificar', methods=['GET','POST'])
def eliminar_pelicula():
    if request.method == 'POST':
        id_pelicula = request.form.get('id_pelicula')
        return redirect(url_for('pelicula.eliminar_pelicula_id', id=id_pelicula))

    return render_template('ingresa_id_pelicula.html')


@pelicula_blueprint.route('/eliminar/<int:id>', methods=['GET','POST'])
def eliminar_pelicula_id(id):
    pelicula = Pelicula.query.get.id(id)

    if not pelicula:
        flash('Pelicula no encontrada o ID invalido', 'error')
        return render_template('ingresa_id_pelicula')

    if request.method == 'GET':
        return render_template('eliminar_pelicula.html', pelicula=pelicula)

    else:
        db.session.delete(pelicula)
        db.session.commit()
        flash('Pelicula eliminada', 'success')
        return redirect(url_for('pelicula.ver_peliculas'))
        
