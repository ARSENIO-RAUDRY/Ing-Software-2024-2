import React from "react";
import {Link} from "react-router-dom";

const Home = (props) => {
    return (
	<div>
	    <h1>CLONEBUSTER</h1>
	    <ul>
		<li> <Link to="/usuarios">Consultar Usuarios</Link></li>
		<li> <Link to="/usuarios/agregar">Agregar Usuarios</Link></li>
	    </ul>
	</div>
    );
}
export default Home;
