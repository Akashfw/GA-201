import logo from './logo.svg';
import './App.css';
import React, {useState} from 'react'

function App() {
   const [post, setPost] = useState([]);

   const handlePost= (event)=>{
     event.preventDefault();
     const username= event.target.username.value;
     const caption = event.target.caption.value

     const newPost = {
      id:Date.now(),
      username,
      caption,
      likes:0,
      Comments:[]
    };
    setPost([...post, newPost])
    event.target.reset();
   };

   

  


  return (
    <div className="App">
      <h1>Instagram App</h1>
    
    <form onSubmit={handlePost}>
      <input type="text" name='username'></input>
    </form>

    </div>
  );
}

export default App;
