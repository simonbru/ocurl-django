import './common'

import React from 'react'
import ReactDOM from "react-dom"


function Hello({ name }) {
  return <span>
    Je suis <strong>{ name }</strong>
  </span>
}


document.addEventListener('DOMContentLoaded', () => {
  ReactDOM.render(
    <Hello name="OCurl"/>,
    document.getElementById('hello')
  )
})
