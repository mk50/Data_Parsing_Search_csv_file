import React,{useState,useEffect} from "react";
import Datatable from "./datatable"
import axios from 'axios'
require("es6-promise").polyfill()
require("isomorphic-fetch");
 function App (){
   const[data,setData]=useState([])
   const [q,setQ]=useState("")

   useEffect(()=>{
  
  //  fetch("https://www.breakingbadapi.com/api/characters/?")
  fetch("./components/data/pythonJSON.json")
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
      <div className="title" style={{fontSize:40,textAlign:"center",}}>serach movies data</div>
    <div>
      <input  type="text" style={{width:500,marginLeft:"430px",marginTop:"20px",height:"30px"}} placeholder="serch movies" value={q} onChange={(e)=>setQ(e.target.value)}/>
 
    </div>
     
      <div>
        <Datatable data={search(data)}/>
      </div>
    </div>
  );
};
export default App;