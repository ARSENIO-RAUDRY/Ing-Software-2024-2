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
            <UsuarioForm onGuardarUsuario={guardaUsuarioHandler} />
        </div>
    )
}

export default CreaUsuario;
