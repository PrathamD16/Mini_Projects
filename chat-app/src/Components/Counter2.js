import React, { useState } from 'react'


function Counter2() {
  // const [count,setCount] = useState(0);
  const [count,setCount] = useState({firstCounter: 0, seconCounter: 0});
  function f1(e){
    let name = e.target.className
    if(name === 'inc'){
      setCount(count.firstCounter++)
    }
  }

  return (
    <div>
      {/* <h1>You Clicked: {count}</h1>
      <button onClick={()=>setCount(count+1)}>Increment by 1</button> */}
      <h1>You clicked:  {count.firstCounter}</h1>
      <button className='inc' onClick={f1}>Increment by 1</button>
    </div>
  )
}

export default Counter2