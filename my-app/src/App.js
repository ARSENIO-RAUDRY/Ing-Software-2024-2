import React, {useState} from "react";
import {BrowserRouter, Routes, Route} from "react-router-dom"
import Home from "./components/Home/Home";
import MuestraUsuarios from "./components/Usuarios/MuestraUsuarios"
import CreaUsuario from "./components/Usuarios/CreaUsuario"

//import "./App.css";

//import Alumnos from "./components/Alumnos/Alumnos";
//import NuevoAlumno from "./components/NuevoAlumno/NuevoAlumno";

function App() {

    /*
    const [alumnos, setAlumnos] = useState([
    {
      nombre: "Fernando",
      apellido: "Fong",
      numCta: 313320679,
    },
    {
      nombre: "Valeria",
      apellido: "Garcia",
      numCta: 314006088,
    },
    {
      nombre: "Erick",
      apellido: "Martinez",
      numCta: 414890123,
    },
  ]);
  const agregarAlumno = (alumno) => {
    const nuevoAlumno = [alumno, ...alumnos];
    setAlumnos(nuevoAlumno);
    console.log(nuevoAlumno);
  };
*/

    const [usuarios, setUsuarios] = useState([
	{
	    id: 1,
	    nombre: "Maluma",
	    apPat: "Vacheron",
	    apMat: "Ozuna",
	    email: "parseadora123@gmail.com",
	    password: "malumababy",
	    superUser: "0"
	},
        {
	    id: 2,
	    nombre: "Sergio",
	    apPat: "Arjona",
	    apMat: "Jimenez",
	    email: "afedo@proton.me",
	    password: "1234",
	    superUser: 1
	},	
        {
	    id: 3,
	    nombre: "Arturo",
	    apPat: "Gutierrez",
	    apMat: "Penaloza",
	    email: "artware@yahoo.com",
	    password: "galspanik",
	    superUser: 0
	}
]);
    const agregarUsuario =(usuario) => {
	const nuevoUsuario = [usuario, ...usuarios];
	setUsuarios(nuevoUsuario);
	console.log(nuevoUsuario);
    }
  return(
      <BrowserRouter>
	  <Routes>
	      <Route path="/" element={<Home />} />
	      <Route path="/usuarios" element={<MuestraUsuarios usuarios={usuarios}/>} />
	      <Route path="/usuarios/agregar" element={<CreaUsuario onAgregarUsuario={agregarUsuario}/>} />	      
	  </Routes>
      </BrowserRouter>
  );
    
  /* return (
    <div className="App">
      <NuevoAlumno onAgregarAlumno={agregarAlumno} />
      <Alumnos alumnos={alumnos} />
    </div>
  );*/
}

export default App;
