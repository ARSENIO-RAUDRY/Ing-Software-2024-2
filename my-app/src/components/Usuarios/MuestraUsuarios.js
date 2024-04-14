import React from "react";

//import Card from '../UI/Card';
import Usuario from "./Usuario/Usuario";
//import './Alumnos.css';

const MuestraUsuarios = ({usuarios}) => {  
    return (
        <div>
            <h1>Lista de Usuarios registrados</h1>
	    <ul>
		{usuarios.map(usuario => (
		    <Usuario key={usuario.idUsuario} usuario={usuario} />
		))}
	    </ul>
        </div>
    );
}

export default MuestraUsuarios;
