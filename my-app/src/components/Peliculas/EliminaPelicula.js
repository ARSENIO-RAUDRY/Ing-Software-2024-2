import React, {useState} from "react";
import {useNavigate} from "react-router-dom";

const EliminaPelicula = ({onEliminarPelicula}) => {
    const navigate = useNavigate('');
    const [idPelicula, setIdPelicula] = useState('');

    const idPeliculaHandler = (event) => {
	setIdPelicula(event.target.value);
    };

    const submitHandler = (event) => {
	event.preventDefault();
	console.log(idPelicula);
	onEliminarPelicula(idPelicula);
	navigate('/peliculas');
    }

    return (
	<div>
   <h1>Eliminar Pelicula</h1>  
   <form onSubmit={submitHandler}>
      <div>
        <div>
          <label>Id del pelicula a eliminar: </label>
          <input
            type="text"
	    name="idPelicula"
	    id="idPelicula"  
            value={idPelicula}
            onChange={idPeliculaHandler} required
          />
        </div>	  
        <div>
          <button type="submit">Eliminar Pelicula</button>
        </div>
      </div>
   </form>
</div>
    );
}
export default EliminaPelicula;
