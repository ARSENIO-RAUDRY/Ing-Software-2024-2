import React, {useState} from "react";
import {useNavigate} from "react-router-dom";

const EliminaUsuario = ({onEliminarUsuario}) => {
    const navigate = useNavigate('');
    const [idUsuario, setIdUsuario] = useState('');

    const idUsuarioHandler = (event) => {
	setIdUsuario(event.target.value);
    };

    const submitHandler = (event) => {
	event.preventDefault();
	console.log(idUsuario);
	onEliminarUsuario(idUsuario);
	navigate('/usuarios');
    }

    return (
	<div>
   <h1>Eliminar Usuario</h1>  
   <form onSubmit={submitHandler}>
      <div>
        <div>
          <label>Id del usuario a eliminar: </label>
          <input
            type="text"
	    name="idUsuario"
	    id="idUsuario"  
            value={idUsuario}
            onChange={idUsuarioHandler} required
          />
        </div>	  
        <div>
          <button type="submit">Eliminar Usuario</button>
        </div>
      </div>
   </form>
</div>
    );
}
export default EliminaUsuario;
