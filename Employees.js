import React from 'react'

import { useSearchParams } from 'react-router-dom'

function Employees() {
  const [searchParams] = useSearchParams()

  const selectedEid = searchParams.get('eid')

  const selectedEmployee = EmployeeData.filter((element) => {
    return element?.empid === selectedEid
  })

  return <h1 style={{ color: 'green' }}>{selectedEmployee[0]?.name}</h1>
}

export default Employees

const EmployeeData = [
  { empid: '100', name: 'Virat' },
  { empid: '200', name: 'Rohit' },
]
