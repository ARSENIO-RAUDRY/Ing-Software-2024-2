import React, { useState } from "react";
import {useNavigate} from "react-router-dom";

const ModificaPelicula = ({peliculas, onModificarPelicula}) => {
  const [idIngresado, setIdIngresado] = useState("");
  const [nombreIngresado, setNombreIngresado] = useState("");
  const [generoIngresado, setGeneroIngresado] = useState("");
  const [duracionIngresado, setDuracionIngresado] = useState("");
  const [inventarioIngresado, setInventarioIngresado] = useState("");

  const navigate = useNavigate('');
    
  const cambioIdHandler = (event) => {
    setIdIngresado(event.target.value);
  };
    
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

    function getPelicula(idPelicula){
	const pelicula = peliculas.find(pelicula => pelicula.idPelicula === parseInt(idPelicula));
	return pelicula || null;
    }
    
  const submitHandler = (event) => {
   event.preventDefault();
   const peliculaModificado = getPelicula(idIngresado);

   if(peliculaModificado){
       const nuevosDatos = {
	   idPelicula: parseInt(idIngresado),
	   nombre: nombreIngresado || peliculaModificado.nombre,
	   genero: generoIngresado || peliculaModificado.genero,
	   duracion: duracionIngresado || peliculaModificado.duracion,
	   inventario: inventarioIngresado || peliculaModificado.inventario
       };
       onModificarPelicula(nuevosDatos);
   } else {
       console.log("Pelicula no encontrada");
   }
      navigate('/peliculas')
   }

  return (
  <div>
   <h1>Modificar Pelicula</h1>  
   <form onSubmit={submitHandler}>
      <div>
        <div>
          <label>Id del pelicula a modificar: </label>
          <input
            type="text"
	    name="idPelicula"
	    id="idPelicula"  
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
          <label>Nuevo Genero: </label>
          <input
            type="text"
	    name="genero"
	    id="genero"  
            value={generoIngresado}
            onChange={cambioGeneroHandler}
          />
        </div>
	  
        <div>
          <label>Nueva Duracion: </label>
          <input
            type="number"
	    name="duracion"
	    id="duracion"  
            value={duracionIngresado}
            onChange={cambioDuracionHandler}
          />
        </div>

        <div>
          <label>Nuevo Inventario: </label>
          <input
            type="number"
            name="inventario"
	    id="inventario"  
            value={inventarioIngresado}
            onChange={cambioInventarioHandler}
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

export default ModificaPelicula;
