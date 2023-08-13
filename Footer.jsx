import React from "react";

export function Footer() {
  var currYear = new Date().getFullYear(); 

  return ( 
    <footer>
      <p>Copyright @ {currYear}</p>
    </footer>
  );
}