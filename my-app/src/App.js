import React, {useState} from "react";
import {BrowserRouter, Routes, Route} from "react-router-dom"

import Home from "./components/Home/Home";

import MuestraUsuarios from "./components/Usuarios/MuestraUsuarios"
import CreaUsuario from "./components/Usuarios/CreaUsuario"
import ModificaUsuario from "./components/Usuarios/ModificaUsuario"
import EliminaUsuario from "./components/Usuarios/EliminaUsuario"

import MuestraPeliculas from "./components/Peliculas/MuestraPeliculas"
import CreaPelicula from "./components/Peliculas/CreaPelicula"
import ModificaPelicula from "./components/Peliculas/ModificaPelicula"
import EliminaPelicula from "./components/Peliculas/EliminaPelicula"

import MuestraRentas from "./components/Rentas/MuestraRentas"
import CreaRenta from "./components/Rentas/CreaRenta"
import ModificaRenta from "./components/Rentas/ModificaRenta"

function App() {
    const [usuarios, setUsuarios] = useState([
	{
	    idUsuario: 1,
	    nombre: "Maluma",
	    apPat: "Vacheron",
	    apMat: "Ozuna",
	    email: "parseadora123@gmail.com",
	    password: "malumababy",
	    superUser: "0"
	},
        {
	    idUsuario: 2,
	    nombre: "Sergio",
	    apPat: "Arjona",
	    apMat: "Jimenez",
	    email: "afedo@proton.me",
	    password: "1234",
	    superUser: 1
	},	
        {
	    idUsuario: 3,
	    nombre: "Arturo",
	    apPat: "Gutierrez",
	    apMat: "Penaloza",
	    email: "artware@yahoo.com",
	    password: "galspanik",
	    superUser: 0
	}
]);

    const [idUsuario, setIdUsuario] = useState(4);

    function incrementaIdUsuario(){
	const idIncrementado = idUsuario + 1;
	setIdUsuario(idIncrementado);
    }
    
    const agregarUsuario =(usuario) => {
	const nuevoUsuario = [usuario, ...usuarios];
	setUsuarios(nuevoUsuario);
	console.log(nuevoUsuario);
    }
    const modificarUsuario = (usuarioModificado) => {
	const usuariosModificados = usuarios.map(usuario =>
	    usuario.idUsuario === usuarioModificado.idUsuario ? usuarioModificado : usuario
	);
	setUsuarios(usuariosModificados);
    };

    const eliminarUsuario = (idUsuario) => {
	setUsuarios((usuarios) => usuarios.filter((usuario) => usuario.idUsuario !== parseInt(idUsuario)));
    }

    const [peliculas, setPeliculas] = useState([
	{
	    idPelicula: 1,
	    nombre: "Ozuna The Animated Movie",
	    genero: "Romance",
	    duracion: 130,
	    inventario:5
	},
        {
	    idPelicula: 2,
	    nombre: "The American Society of Magical Nerds",
	    genero: "Drama",
	    duracion: 140,
	    inventario: 10
	},	
        {
	    idPelicula: 3,
	    nombre: "El Santo contra la Facultad de Ingenieria",
	    genero: "Terror",
	    duracion: 90,
	    inventario: 3
	}
]);

    const [idPelicula, setIdPelicula] = useState(4);

    function incrementaIdPelicula(){
	const idIncrementado = idPelicula + 1;
	setIdPelicula(idIncrementado);
    }
    
    const agregarPelicula =(pelicula) => {
	const nuevoPelicula = [pelicula, ...peliculas];
	setPeliculas(nuevoPelicula);
	console.log(nuevoPelicula);
    }
    const modificarPelicula = (peliculaModificado) => {
	const peliculasModificados = peliculas.map(pelicula =>
	    pelicula.idPelicula === peliculaModificado.idPelicula ? peliculaModificado : pelicula
	);
	setPeliculas(peliculasModificados);
    };

    const eliminarPelicula = (idPelicula) => {
	setPeliculas((peliculas) => peliculas.filter((pelicula) => pelicula.idPelicula !== parseInt(idPelicula)));
    }

        const [rentas, setRentas] = useState([
	{
	    idRentar: 1,
	    idUsuario: 1,
	    idPelicula: 1,
	    fecha_renta: "2024-04-13",
	    dias_de_renta: 5,
	    estatus: 0
	},
        {
	    idRentar: 2,
	    idUsuario: 2,
	    idPelicula: 2,
	    fecha_renta: "2024-04-09",
	    dias_de_renta: 10,
	    estatus: 1
	},	
        {
	    idRentar: 3,
	    idUsuario: 3,
	    idPelicula: 3,
	    fecha_renta: "2024-04-08",
	    dias_de_renta: 7,
	    estatus: 0
	}
]);

    const [idRenta, setIdRenta] = useState(4);

    function incrementaIdRenta(){
	const idIncrementado = idRenta + 1;
	setIdRenta(idIncrementado);
    }
    
    const agregarRenta =(renta) => {
	const nuevoRenta = [renta, ...rentas];
	setRentas(nuevoRenta);
	console.log(nuevoRenta);
    }
    const modificarRenta = (rentaModificado) => {
	const rentasModificados = rentas.map(renta =>
	    renta.idRenta === rentaModificado.idRenta ? rentaModificado : renta
	);
	setRentas(rentasModificados);
    };

    const eliminarRenta = (idRentar) => {
	setRentas((rentas) => rentas.filter((renta) => renta.idRentar !== parseInt(idRentar)));
    }
    
    return(
      <BrowserRouter>
	  <Routes>
	      <Route path="/" element={<Home />} />
	      <Route path="/usuarios" element={<MuestraUsuarios usuarios={usuarios}/>} />
	      <Route path="/usuarios/agregar" element={<CreaUsuario onAgregarUsuario={agregarUsuario}/>} />
	      <Route path="/usuarios/modificar" element={<ModificaUsuario usuarios={usuarios} onModificarUsuario={modificarUsuario}/>} />
	      <Route path="/usuarios/eliminar" element={<EliminaUsuario  onEliminarUsuario={eliminarUsuario}/>} />

	      <Route path="/peliculas" element={<MuestraPeliculas peliculas={peliculas}/>} />
	      <Route path="/peliculas/agregar" element={<CreaPelicula onAgregarPelicula={agregarPelicula}/>} />
	      <Route path="/peliculas/modificar" element={<ModificaPelicula peliculas={peliculas} onModificarPelicula={modificarPelicula}/>} />
	      <Route path="/peliculas/eliminar" element={<EliminaPelicula  onEliminarPelicula={eliminarPelicula}/>} />

	      <Route path="/rentas" element={<MuestraRentas rentas={rentas}/>} />
	      <Route path="/rentas/agregar" element={<CreaRenta onAgregarRenta={agregarRenta}/>} />
	      <Route path="/rentas/modificar" element={<ModificaRenta rentas={rentas} onModificarRenta={modificarRenta}/>} />
	  </Routes>
      </BrowserRouter>
  );
}

export default App;
