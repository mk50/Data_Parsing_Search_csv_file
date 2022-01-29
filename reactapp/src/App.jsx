import React,{useState,useEffect} from "react";
import Datatable from "./datatable"
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
 function App (){
   const[data,setData]=useState([])
   const [q,setQ]=useState("")
   useEffect(()=>{
  //  fetch('https://www.breakingbadapi.com/api/characters/?') #### ممكن استخدم endpoint  مثل breakingbad end point
  fetch("../public/pythonJSON.json")   // json file path
  .then((response)=>response.json())
  .then((json)=>setData( json))
  

   },[])
             // make search by any value 
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
      <div>
        <Datatable data={search(data)}/>
      </div>
    </div>
  );
};
export default App;