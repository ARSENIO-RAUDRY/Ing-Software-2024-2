import React, { useState } from "react";

//import "./AlumnoForm.css";

const PeliculaForm = (props) => {
  const [nombreIngresado, setNombreIngresado] = useState("");
  const [generoIngresado, setGeneroIngresado] = useState("");
  const [duracionIngresado, setDuracionIngresado] = useState("");
  const [inventarioIngresado, setInventarioIngresado] = useState("");

  const cambioNombreHandler = (event) => {
    setNombreIngresado(event.target.value);
  };

  const cambioGeneroHandler = (event) => {
    setGeneroIngresado(event.target.value);
  };

  const cambioDuracionHandler = (event) => {
    setDuracionIngresado(event.target.value);
  };    

  const cambioInventarioHandler = (event) => {
    setInventarioIngresado(event.target.value);
  };
    
  const submitHandler = (event) => {
    event.preventDefault();

    const pelicula = {
      nombre: nombreIngresado,
      genero: generoIngresado,
      duracion: duracionIngresado,
      inventario: inventarioIngresado
    };

      if (
      nombreIngresado === "" ||
      generoIngresado === "" ||
      duracionIngresado === "" ||
      inventarioIngresado === ""
    ) {
      alert("Campos vacíos!!");
      return;
    }
    props.onGuardarPelicula(pelicula);
    setNombreIngresado("");
    setGeneroIngresado("");
    setDuracionIngresado("");
    setInventarioIngresado("");
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
          <label>Genero: </label>
          <input
            type="text"
            value={generoIngresado}
            onChange={cambioGeneroHandler}
          />
        </div>
	  
        <div>
          <label>Duracion: </label>
          <input
            type="number"
            value={duracionIngresado}
            onChange={cambioDuracionHandler}
          />
        </div>

        <div>
          <label>Inventario: </label>
          <input
            type="number"
            value={inventarioIngresado}
            onChange={cambioInventarioHandler}
          />
        </div>	  
	  
        <div>
          <button type="submit">Agregar Pelicula</button>
        </div>
      </div>
    </form>
  );
};

export default PeliculaForm;
