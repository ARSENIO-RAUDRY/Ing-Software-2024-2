import React from "react";

//import './Usuario.css';

const Usuario = ({usuario}) => {
    return (
	<li key={usuario.idUsuario}>
                <h2>{usuario.nombre}</h2>
                <h2>{usuario.apPat}</h2>
                <h2>{usuario.apMat}</h2>
                <h2>{usuario.password}</h2>
                <h2>{usuario.email}</h2>
                <h2>{usuario.superUser}</h2>
        </li>
    );
}

export default Usuario
