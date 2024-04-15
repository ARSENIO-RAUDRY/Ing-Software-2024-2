import React from "react";
import Renta from "./Renta/Renta";
//import './Alumnos.css';

const MuestraRentas = ({rentas}) => {  
    return (
        <div>
            <h1>Lista de Rentas registrados</h1>
	    <ul>
		{rentas.map(renta => (
		    <Renta key={renta.idRenta} renta={renta} />
		))}
	    </ul>
        </div>
    );
}

export default MuestraRentas;
