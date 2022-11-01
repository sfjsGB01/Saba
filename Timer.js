import React, { useState, useEffect } from 'react'

function Timer() {
  const [currentTime, setCurrentTime] = useState(
    new Date().toLocaleTimeString()
  )

  useEffect(() => {
    console.log('Component is mounted')

    const timer = setInterval(() => {
      console.log('***RUNNING SET INTERVAL****')
      setCurrentTime(new Date().toLocaleTimeString())
    }, 1000)

    return () => {
      console.log('Component is unmounted')
      clearInterval(timer)
    }
  }, [])

  console.log('Rendering component...')
  return (
    <div>
      <h1>Current Time Page</h1>
      <h2>{currentTime}</h2>
    </div>
  )
}

export default Timer
