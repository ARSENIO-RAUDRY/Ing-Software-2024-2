import React from "react";

//import './NuevoAlumno.css';
import PeliculaForm from "./PeliculaForm/PeliculaForm";

const CreaPelicula = (props) => {
    
    const guardaPeliculaHandler = (peliculaIngresado) => {
        const peliculas = { 
            ...peliculaIngresado
        };
        props.onAgregarPelicula(peliculas);
    };

    return (
        <div>
	    <h1>Crea Nueva Pelicula</h1>
            <PeliculaForm onGuardarPelicula={guardaPeliculaHandler} />
        </div>
    )
}

export default CreaPelicula;
