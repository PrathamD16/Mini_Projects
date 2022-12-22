import React, { useReducer } from 'react'

const initialState = {
    count: 0,
};
const f1 = (curr,action) => {
    switch(action.type){
        case 'incr1':
            return {count: curr.count+action.value};
        case 'decr1':
            return {count: curr.count-action.value};
    }
}

function Counter() {
    const [count,dispatch] = useReducer(f1,initialState);
  return (
    <div>
        <h1>Count: {count.count}</h1>
        <button onClick={()=>dispatch({type:'incr1', value: 1})}>Increment by 1</button>
        <button onClick={()=>dispatch({type:'decr1', value: 2})}>Decrement by 2</button>

    </div>
  )
}

export default Counter