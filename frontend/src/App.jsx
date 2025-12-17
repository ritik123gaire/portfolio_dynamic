import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className='w-1/2 mx-auto text-center text-5xl'>
      Home
    </div>
  )
}

export default App
