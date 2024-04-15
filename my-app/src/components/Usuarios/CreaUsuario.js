import React from "react";

//import './NuevoAlumno.css';
import UsuarioForm from "./UsuarioForm/UsuarioForm";

const CreaUsuario = (props) => {
    
    const guardaUsuarioHandler = (usuarioIngresado) => {
        const usuarios = { 
            ...usuarioIngresado
        };
        props.onAgregarUsuario(usuarios);
    };

    return (
        <div>
	    <h1>Crea Nuevo Usuario</h1>
            <UsuarioForm onGuardarUsuario={guardaUsuarioHandler} />
        </div>
    )
}

export default CreaUsuario;
