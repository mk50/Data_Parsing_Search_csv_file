import React from 'react';

export default function Datatable({data}) {
    const columns=data[0] && Object.keys(data[0]);
  return (<table cellPadding={0} cellSpacing={0} style={{width:"500px",height:"700px"}}>
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

  </table>
  );
}