import React from "react";
import { useState } from "react";

export const AddTodo = (props) => {
  const [title, settitle] = useState("");
  const [desc, setDesc] = useState("");

  const submit = (e) => {
    e.preventDefault();
    if (!title || !desc) {
      alert("Title or Description cannot be blank");
    } else {
      setDesc("");
      settitle("");

      props.addTodo(title, desc);
    }
  };

  return (
    <div className="container">
      <h3 className="my-3">Add a Todo</h3>
      <form onSubmit={submit}>
        <div className="mb-3">
          <label htmlFor="exampleInputEmail1" className="form-label">
            ToDo Title
          </label>
          <input
            type="text"
            className="form-control"
            id="exampleInputEmail1"
            aria-describedby="emailHelp"
            value={title}
            onChange={(e) => {
              settitle(e.target.value);
            }}
          />
        </div>
        <div className="mb-3">
          <label htmlFor="desc" className="form-label">
            Description
          </label>
          <input
            type="text"
            className="form-control"
            id="desc"
            value={desc}
            onChange={(e) => {
              setDesc(e.target.value);
            }}
          />
        </div>
        <button type="submit" className="btn btn-primary">
          Add todo
        </button>
      </form>
    </div>
  );
};
