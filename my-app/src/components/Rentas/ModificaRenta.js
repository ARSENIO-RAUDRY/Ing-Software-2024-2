import React, { useState } from "react";
import {useNavigate} from "react-router-dom";

const ModificaRenta = ({rentas, onModificarRenta}) => {
  const [idIngresado, setIdIngresado] = useState("");
  const [estatusIngresado, setEstatusIngresado] = useState("");    
  const navigate = useNavigate('');   

  const cambioIdHandler = (event) => {
    setIdIngresado(event.target.value);
  };
    
  const cambioEstatusHandler = (event) => {
    setEstatusIngresado(event.target.value);
  };

    function getRenta(idRenta){
	const renta = rentas.find(renta => renta.idRenta === parseInt(idRenta));
	return renta || null;
    }
    
  const submitHandler = (event) => {
   event.preventDefault();
   const rentaModificado = getRenta(idIngresado);

   if(rentaModificado){
       const nuevosDatos = {
	   idRenta: parseInt(idIngresado),
	   idUsuario: rentaModificado.idUsuario,
	   idPelicula: rentaModificado.idPelicula,
	   fecha_renta: rentaModificado.fecha_renta,
	   dias_de_renta: rentaModificado.dias_de_renta,
	   estatus: estatusIngresado,
       };
       onModificarRenta(nuevosDatos);
   } else {
       console.log("Renta no encontrado");
   }
      navigate('/rentas')
   }

  return (
  <div>
   <h1>Modificar Renta</h1>  
   <form onSubmit={submitHandler}>
      <div>
        <div>
          <label>Id de la renta a modificar: </label>
          <input
            type="text"
	    name="idRenta"
	    id="idRenta"  
            value={idIngresado}
            onChange={cambioIdHandler} required
          />
        </div>       
	<div>
          <label>Ha sido devuelta: </label>
          <input
            type="checkbox"
	    name="estatus"
	    id="estatus"  
            value={estatusIngresado}
            onChange={cambioEstatusHandler}
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

export default ModificaRenta;
