import React from "react";

//import './NuevoAlumno.css';
import RentaForm from "./RentaForm/RentaForm";

const CreaRenta = (props) => {
    
    const guardaRentaHandler = (rentaIngresado) => {
        const rentas = { 
            ...rentaIngresado
        };
        props.onAgregarRenta(rentas);
    };

    return (
        <div>
	    <h1>Crea Nuevo Renta</h1>
            <RentaForm onGuardarRenta={guardaRentaHandler} />
        </div>
    )
}

export default CreaRenta;
