import React,{useState,useEffect} from "react";
import Datatable from "./datatable"
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
import axios from 'axios'
require('bootstrap/dist/css/bootstrap.css');
require("es6-promise").polyfill()
require("isomorphic-fetch");
 function App (){
   const[data,setData]=useState([])
   const [q,setQ]=useState("")

   useEffect(()=>{
  
  //  fetch("https://www.breakingbadapi.com/api/characters/?")
  // fetch("./components/data/pythonJSON.json")
  fetch("https://www.breakingbadapi.com/api/characters/?")
  .then((response)=>response.json())
  .then((json)=>setData(json))

    // axios.get("./components/data/dataf.json")
    // .then(response => {
    //  console.log(response)
    //   setData(response.data)

   
   },[])
  


    
  function search(rows){
     const columns=rows[0] && Object.keys(rows[0])
     return rows.filter((row)=>
     columns.some(
       (column)=>row[column].toString().toLowerCase().indexOf(q.toLowerCase())> -1)
   
     );
   }


   return (
    <div className="App">
    

    
  
   <div style={{textAlign:"center",marginTop:"25px"}}>
     <h1>Search on movies</h1>
   </div>
    
     
     <Col xs={5} >
       <Form.Control placeholder="Search anything in movies"   value={q} onChange={(e)=>setQ(e.target.value)} style={{marginLeft:"400px"}} />
       
      </Col>
    
      {/* <button type="button" className="btn btn-warning">
          <svg width="15px" height="15px">
        <path d="M11.618 9.897l4.224 4.212c.092.09.1.23.02.312l-1.464 1.46c-.08.08-.222.072-.314-.02L9.868 11.66M6.486 10.9c-2.42 0-4.38-1.955-4.38-4.367 0-2.413 1.96-4.37 4.38-4.37s4.38 1.957 4.38 4.37c0 2.412-1.96 4.368-4.38 4.368m0-10.834C2.904.066 0 2.96 0 6.533 0 10.105 2.904 13 6.486 13s6.487-2.895 6.487-6.467c0-3.572-2.905-6.467-6.487-6.467 "></path>
      </svg>
       </button> */}
         
     
      <div>
        <Datatable data={search(data)}/>
      </div>
    </div>
  );
};
export default App;