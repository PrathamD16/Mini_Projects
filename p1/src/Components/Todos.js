import React from "react";
import TodoItems from "./TodoItems";

function Todos(props) {

  const myStyle = {
    minHeight: '70vh',
     

  }

  return (
    <div className="container my-3" style={myStyle}>
        <h3 className="my-3">Todo List</h3>
        {props.todos.length == 0 ? <h2>No Todos to display</h2> : props.todos.map((task) => {
          return <>
          <TodoItems todo={task} key={task.sno} onDelete={props.onDelete} /><hr/>
          </> 
        })}
    </div>
  );
}

export default Todos; 
