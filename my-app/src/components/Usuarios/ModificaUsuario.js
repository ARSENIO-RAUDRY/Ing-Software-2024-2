import React, { useState } from "react";
import {useNavigate} from "react-router-dom";

const ModificaUsuario = ({usuarios, onModificarUsuario}) => {
  const [idIngresado, setIdIngresado] = useState("");
  const [nombreIngresado, setNombreIngresado] = useState("");
  const [apPatIngresado, setApPatIngresado] = useState("");
  const [apMatIngresado, setApMatIngresado] = useState("");
  const [passwordIngresado, setPasswordIngresado] = useState("");
  const [emailIngresado, setEmailIngresado] = useState("");    
  const [superUserIngresado, setSuperUserIngresado] = useState("");
  const navigate = useNavigate('');
    
  const cambioIdHandler = (event) => {
    setIdIngresado(event.target.value);
  };
    
  const cambioNombreHandler = (event) => {
    setNombreIngresado(event.target.value);
  };

  const cambioApPatHandler = (event) => {
    setApPatIngresado(event.target.value);
  };

  const cambioApMatHandler = (event) => {
    setApMatIngresado(event.target.value);
  };    

  const cambioPasswordHandler = (event) => {
    setPasswordIngresado(event.target.value);
  };

  const cambioEmailHandler = (event) => {
    setEmailIngresado(event.target.value);
  };

  const cambioSuperUserHandler = (event) => {
    setSuperUserIngresado(event.target.value);
  };

    function getUsuario(idUsuario){
	const usuario = usuarios.find(usuario => usuario.idUsuario === parseInt(idUsuario));
	return usuario || null;
    }
    
  const submitHandler = (event) => {
   event.preventDefault();
   const usuarioModificado = getUsuario(idIngresado);

   if(usuarioModificado){
       const nuevosDatos = {
	   idUsuario: parseInt(idIngresado),
	   nombre: nombreIngresado || usuarioModificado.nombre,
	   apPat: apPatIngresado || usuarioModificado.apPat,
	   apMat: apMatIngresado || usuarioModificado.apMat,
	   password: passwordIngresado || usuarioModificado.password,
	   email: emailIngresado || usuarioModificado.email,
	   superUser: superUserIngresado || usuarioModificado.superUser
       };
       onModificarUsuario(nuevosDatos);
   } else {
       console.log("Usuario no encontrado");
   }
      navigate('/usuarios')
   }

  return (
  <div>
   <h1>Modificar Usuario</h1>  
   <form onSubmit={submitHandler}>
      <div>
        <div>
          <label>Id del usuario a modificar: </label>
          <input
            type="text"
	    name="idUsuario"
	    id="idUsuario"  
            value={idIngresado}
            onChange={cambioIdHandler} required
          />
        </div>
        <div>
          <label>Nuevo nombre: </label>
          <input
            type="text"
	    name="nombre"
	    id="nombre"  
            value={nombreIngresado}
            onChange={cambioNombreHandler}
          />
        </div>
	  
        <div>
          <label>Nuevo Apellido Paterno: </label>
          <input
            type="text"
	    name="apPat"
	    id="apPat"  
            value={apPatIngresado}
            onChange={cambioApPatHandler}
          />
        </div>
	  
        <div>
          <label>Apellido Materno: </label>
          <input
            type="text"
	    name="apMat"
	    id="apMat"  
            value={apMatIngresado}
            onChange={cambioApMatHandler}
          />
        </div>

        <div>
          <label>Password: </label>
          <input
            type="password"
            name="password"
	    id="password"  
            value={passwordIngresado}
            onChange={cambioPasswordHandler}
          />
        </div>	  

	<div>
          <label>Email: </label>
          <input
            type="email"
	    name="email"
	    id="email"  
            value={emailIngresado}
            onChange={cambioEmailHandler}
          />
        </div>

        <div>
          <label>SuperUser: </label>
          <input
            type="checkbox"
	    name="superUser"
	    id="superUser"  
            value={superUserIngresado}
            onChange={cambioSuperUserHandler}
          />
        </div>
	  
        <div>
          <button type="submit">Guardar Cambios</button>
        </div>
      </div>
   </form>
</div>    
  );
};

export default ModificaUsuario;
