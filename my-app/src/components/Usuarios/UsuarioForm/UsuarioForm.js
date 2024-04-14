import React, { useState } from "react";

//import "./AlumnoForm.css";

const UsuarioForm = (props) => {
  const [nombreIngresado, setNombreIngresado] = useState("");
  const [apPatIngresado, setApPatIngresado] = useState("");
  const [apMatIngresado, setApMatIngresado] = useState("");
  const [passwordIngresado, setPasswordIngresado] = useState("");
  const [emailIngresado, setEmailIngresado] = useState("");    
  const [superUserIngresado, setSuperUserIngresado] = useState("");

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
    
  const submitHandler = (event) => {
    event.preventDefault();

    const usuario = {
      nombre: nombreIngresado,
      apPat: apPatIngresado,
      apMat: apMatIngresado,
      password: passwordIngresado,
      email: emailIngresado,
      superUser: superUserIngresado
    };

      if (
      nombreIngresado === "" ||
      apPatIngresado === "" ||
      apMatIngresado === "" ||
      passwordIngresado === "" ||
      emailIngresado === "" 
    ) {
      alert("Campos vacíos!!");
      return;
    }
    props.onGuardarUsuario(usuario);
    setNombreIngresado("");
    setApPatIngresado("");
    setApMatIngresado("");
    setPasswordIngresado("");
    setEmailIngresado("");
    setSuperUserIngresado("");
  };

  return (
    <form onSubmit={submitHandler}>
      <div>
        <div>
          <label>Nombre: </label>
          <input
            type="text"
            value={nombreIngresado}
            onChange={cambioNombreHandler}
          />
        </div>
	  
        <div>
          <label>Apellido Paterno: </label>
          <input
            type="text"
            value={apPatIngresado}
            onChange={cambioApPatHandler}
          />
        </div>
	  
        <div>
          <label>Apellido Materno: </label>
          <input
            type="text"
            value={apMatIngresado}
            onChange={cambioApMatHandler}
          />
        </div>

        <div>
          <label>Password: </label>
          <input
            type="password"
            value={passwordIngresado}
            onChange={cambioPasswordHandler}
          />
        </div>	  

	<div>
          <label>Email: </label>
          <input
            type="email"
            value={emailIngresado}
            onChange={cambioEmailHandler}
          />
        </div>

        <div>
          <label>SuperUser: </label>
          <input
            type="checkbox"
            value={superUserIngresado}
            onChange={cambioSuperUserHandler}
          />
        </div>
	  
        <div>
          <button type="submit">Agregar Usuario</button>
        </div>
      </div>
    </form>
  );
};

export default UsuarioForm;
