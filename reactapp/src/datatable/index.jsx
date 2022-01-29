import React from 'react';
import {Table}  from 'react-bootstrap';
// import {BootstrapTable} from 'reactjs-bootstrap-table';


export default function Datatable({data}) {
    const columns=data[0] && Object.keys(data[0]);
  return (
  <Table cellPadding={0} cellSpacing={0} striped bordered hover variant="dark" responsive style={{marginTop:"25px"}}>
      <thead>
       <tr>{data[0]&& columns.map((heading)=><th>{heading}</th>)}</tr>
      </thead>
      <tbody>
          {data.map(row=><tr>
              {
                  columns.map(columns=>
                  <td>
                      {
                          row[columns]
                      }
                      </td>)
              }
              </tr>)}

      </tbody>

  </Table>
  );
}



