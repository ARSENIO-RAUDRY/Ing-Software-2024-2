import React from "react";

//import './Usuario.css';

const Usuario = ({usuario}) => {
    return (
	<li key={usuario.idUsuario}>
            <b>Id:</b> {usuario.idUsuario} <br/>
            <b>Nombre:</b> {usuario.nombre} <br/>
            <b>Apellido Paterno:</b> {usuario.apPat} <br/>
            <b>Apellido Materno:</b> {usuario.apMat} <br/>
            <b>Password:</b> {usuario.password} <br/>
            <b>Email:</b> {usuario.email} <br/>
            <b>SuperUsuario:</b> {usuario.superUser} <br/>
        </li>
    );
}

export default Usuario
