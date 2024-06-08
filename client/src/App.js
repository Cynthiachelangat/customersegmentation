import React, { useState } from 'react'
import axios from 'axios'

function App() {
  const [formData, setFormData] = useState({
    BALANCE: '',
    PURCHASES: '',
    ONEOFF_PURCHASES: '',
    INSTALLMENTS_PURCHASES: '',
    CASH_ADVANCE: '',
    PURCHASES_FREQUENCY: '',
    ONEOFF_PURCHASES_FREQUENCY: '',
    PURCHASES_INSTALLMENTS_FREQUENCY: '',
    CASH_ADVANCE_FREQUENCY: '',
    CREDIT_LIMIT: '',
    PAYMENTS: '',
    MINIMUM_PAYMENTS: '',
    PRC_FULL_PAYMENT: '',
    TENURE: '',
  })
  const [result, setResult] = useState(null)

  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData({
      ...formData,
      [name]: value,
    })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      const response = await axios.post('http://127.0.0.1:5000/predict', [
        formData,
      ])
      setResult(response.data)
    } catch (error) {
      console.error('There was an error!', error)
    }
  }

  return (
    <div className="App">
      <h1>Customer Segmentation</h1>
      <form onSubmit={handleSubmit}>
        {Object.keys(formData).map((key) => (
          <div key={key}>
            <label>
              {key}:
              <input
                type="text"
                name={key}
                value={formData[key]}
                onChange={handleChange}
              />
            </label>
          </div>
        ))}
        <button type="submit">Submit</button>
      </form>
      {result && (
        <div>
          <h2>Result</h2>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  )
}

export default App
