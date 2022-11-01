import React from 'react'

import { useParams } from 'react-router-dom'

function Products() {
  const routeParams = useParams()

  const selectedProduct = products.filter((element) => {
    return element?.id === routeParams?.id
  })

  return <h1 style={{ color: 'blue' }}>{selectedProduct[0]?.name}</h1>
}

export default Products

const products = [
  { id: '100', name: 'iPhone' },
  { id: '200', name: 'Android Phone' },
]
