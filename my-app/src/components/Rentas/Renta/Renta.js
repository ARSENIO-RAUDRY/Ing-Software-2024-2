import React from "react";

//import './Renta.css';

const Renta = ({renta}) => {
    return (
	<li key={renta.idRentar}>
            <b>Id:</b> {renta.idRentar} <br/>
            <b>Id Usuario:</b> {renta.idUsuario} <br/>
            <b>Id Pelicula:</b> {renta.idPelicula} <br/>	    
            <b>Fecha:</b> {renta.fecha_renta} <br/>
            <b>Dias de Renta:</b> {renta.dias_de_renta} <br/>
            <b>Estatus:</b> {renta.estatus} <br/>
        </li>
    );
}

export default Renta
