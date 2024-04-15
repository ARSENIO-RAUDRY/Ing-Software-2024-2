import React, { useState } from "react";

//import "./AlumnoForm.css";

const RentaForm = (props) => {
  const [idUsuarioIngresado, setIdUsuarioIngresado] = useState("");
  const [idPeliculaIngresado, setIdPeliculaIngresado] = useState("");
  const [fecha_rentaIngresado, setFecha_RentaIngresado] = useState("");
  const [dias_de_rentaIngresado, setDias_De_RentaIngresado] = useState("");    
  const [estatusIngresado, setEstatusIngresado] = useState("");

  const cambioIdUsuarioHandler = (event) => {
    setIdUsuarioIngresado(event.target.value);
  };

  const cambioIdPeliculaHandler = (event) => {
    setIdPeliculaIngresado(event.target.value);
  };

  const cambioFecha_RentaHandler = (event) => {
    setFecha_RentaIngresado(event.target.value);
  };

  const cambioDias_De_RentaHandler = (event) => {
    setDias_De_RentaIngresado(event.target.value);
  };    

  const cambioEstatusHandler = (event) => {
    setEstatusIngresado(event.target.value);
  };
    
  const submitHandler = (event) => {
    event.preventDefault();
    const renta = {
      idUsuario: parseInt(idUsuarioIngresado),
      idPelicula: parseInt(idPeliculaIngresado),
      fecha_renta: fecha_rentaIngresado,
      dias_de_renta: parseInt(dias_de_rentaIngresado),
      estatus: estatusIngresado
    };

      if (
      idUsuarioIngresado === "" ||
      idPeliculaIngresado === "" ||
      fecha_rentaIngresado === "" ||
      dias_de_rentaIngresado === ""	  
    ) {
      alert("Campos vacíos!!");
      return;
    }
    props.onGuardarRenta(renta);
    setIdUsuarioIngresado("");
    setIdPeliculaIngresado("");
    setFecha_RentaIngresado("");
    setDias_De_RentaIngresado("");
    setEstatusIngresado("");
  };

  return (
    <form onSubmit={submitHandler}>
      <div>
        <div>
          <label>Id Usuario: </label>
          <input
            type="text"
            value={idUsuarioIngresado}
            onChange={cambioIdUsuarioHandler}
          />
        </div>
	  
        <div>
          <label>Id Pelicula: </label>
          <input
            type="text"
            value={idPeliculaIngresado}
            onChange={cambioIdPeliculaHandler}
          />
        </div>
	  
        <div>
          <label>Fecha de Renta: </label>
          <input
            type="date"
            value={fecha_rentaIngresado}
            onChange={cambioFecha_RentaHandler}
          />
        </div>

        <div>
          <label>Dias de Renta: </label>
          <input
            type="number"
            value={dias_de_rentaIngresado}
            onChange={cambioDias_De_RentaHandler}
          />
        </div>	  

        <div>
          <label>Estatus </label>
          <input
            type="checkbox"
            value={estatusIngresado}
            onChange={cambioEstatusHandler}
          />
        </div>
	  
        <div>
          <button type="submit">Agregar Renta</button>
        </div>
      </div>
    </form>
  );
};

export default RentaForm;