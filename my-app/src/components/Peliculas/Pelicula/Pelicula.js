import React from "react";

//import './Pelicula.css';

const Pelicula = ({pelicula}) => {
    return (
	<li key={pelicula.idPelicula}>
            <b>Id:</b> {pelicula.idPelicula} <br/>
            <b>Nombre:</b> {pelicula.nombre} <br/>
            <b>Genero:</b> {pelicula.genero} <br/>
            <b>Duracion:</b> {pelicula.duracion} <br/>
            <b>Inventario:</b> {pelicula.inventario} <br/>
        </li>
    );
}

export default Pelicula
