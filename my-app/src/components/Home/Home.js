import React from "react";
import {Link} from "react-router-dom";

const Home = (props) => {
    return (
	<div>
	    <h1>CLONEBUSTER</h1>
	    <ul>
		<li> <Link to="/usuarios">Consultar Usuarios</Link></li>
		<li> <Link to="/usuarios/agregar">Agregar Usuarios</Link></li>
		<li> <Link to="/usuarios/modificar">Modificar Usuarios</Link></li>
		<li> <Link to="/usuarios/eliminar">Eliminar Usuarios</Link></li>

		<li> <Link to="/peliculas">Consultar Peliculas</Link></li>
		<li> <Link to="/peliculas/agregar">Agregar Peliculas</Link></li>
		<li> <Link to="/peliculas/modificar">Modificar Peliculas</Link></li>
		<li> <Link to="/peliculas/eliminar">Eliminar Peliculas</Link></li>

		<li> <Link to="/rentas">Consultar Rentas</Link></li>
		<li> <Link to="/rentas/agregar">Agregar Rentas</Link></li>
		<li> <Link to="/rentas/modificar">Modificar Rentas</Link></li>
	    </ul>
	</div>
    );
}
export default Home;
