import { useState, useRef, useEffect } from 'react'
import ChatInterface from './components/ChatInterface'
import CodeDisplay from './components/CodeDisplay'
import TestResults from './components/TestResults'
import './App.css'

function App() {
  const [prompt, setPrompt] = useState('')
  const [description, setDescription] = useState('')
  const [loading, setLoading] = useState(false)
  const [executing, setExecuting] = useState(false)
  const [error, setError] = useState('')
  const [response, setResponse] = useState(null)
  const [testResults, setTestResults] = useState(null)
  const [activeTab, setActiveTab] = useState('code')

  const handleGenerate = async (e) => {
    e.preventDefault()
    if (!prompt.trim()) {
      setError('Please enter a prompt')
      return
    }

    setLoading(true)
    setError('')
    setResponse(null)
    setTestResults(null)

    try {
      const res = await fetch('http://localhost:8000/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          prompt: prompt.trim(),
          description: description.trim(),
        }),
      })

      if (!res.ok) {
        throw new Error(`HTTP error! status: ${res.status}`)
      }

      const data = await res.json()
      setResponse(data)
      setPrompt('')
      setDescription('')
    } catch (err) {
      setError(`Error: ${err.message}`)
      console.error('Error:', err)
    } finally {
      setLoading(false)
    }
  }

  const handleExecute = async () => {
    if (!response || !response.code || !response.tests) {
      setError('No code or tests to execute')
      return
    }

    setExecuting(true)
    setError('')
    setTestResults(null)

    try {
      const res = await fetch('http://localhost:8000/execute', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          code: response.code,
          tests: response.tests,
        }),
      })

      if (!res.ok) {
        throw new Error(`HTTP error! status: ${res.status}`)
      }

      const data = await res.json()
      setTestResults(data)
      setActiveTab('results')
    } catch (err) {
      setError(`Execution error: ${err.message}`)
      console.error('Execution error:', err)
    } finally {
      setExecuting(false)
    }
  }

  return (
    <div className="app-container">
      <div className="header">
        <h1>🐕 Pochita</h1>
        <h3>AI Code Generation & Testing Platform</h3>
      </div>

      <div className="form-container">
        <form onSubmit={handleGenerate}>
          <input
            type="text"
            placeholder="Enter your code generation request..."
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            disabled={loading}
            className="input-field"
          />
          <input
            type="text"
            placeholder="(Optional) Additional description or requirements..."
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            disabled={loading}
            className="input-field input-secondary"
          />
          <button type="submit" disabled={loading} className="submit-btn">
            {loading ? 'Generating...' : 'Generate Code'}
          </button>
        </form>
      </div>

      {error && <div className="error-alert">{error}</div>}

      {loading && (
        <div className="loading">
          <div className="spinner"></div>
          <p>Generating code and tests...</p>
        </div>
      )}

      {response && (
        <div className="response-container">
          <div className="tabs-header">
            <div className="tabs">
              <button
                className={`tab-btn ${activeTab === 'code' ? 'active' : ''}`}
                onClick={() => setActiveTab('code')}
              >
                Generated Code
              </button>
              <button
                className={`tab-btn ${activeTab === 'tests' ? 'active' : ''}`}
                onClick={() => setActiveTab('tests')}
              >
                Generated Tests
              </button>
              <button
                className={`tab-btn ${activeTab === 'chat' ? 'active' : ''}`}
                onClick={() => setActiveTab('chat')}
              >
                Conversation
              </button>
              {testResults && (
                <button
                  className={`tab-btn ${activeTab === 'results' ? 'active' : ''}`}
                  onClick={() => setActiveTab('results')}
                >
                  Test Results
                </button>
              )}
            </div>
            <div className="tabs-actions">
              <button
                className="execute-btn"
                onClick={handleExecute}
                disabled={executing || activeTab === 'results'}
              >
                {executing ? 'Running Tests...' : '▶ Run Tests'}
              </button>
            </div>
          </div>

          <div className="tab-content">
            {activeTab === 'code' && (
              <CodeDisplay code={response.code} title="Generated Code" />
            )}
            {activeTab === 'tests' && (
              <CodeDisplay code={response.tests} title="Generated Tests" />
            )}
            {activeTab === 'chat' && (
              <ChatInterface messages={response.conversation} />
            )}
            {activeTab === 'results' && (
              <TestResults
                results={testResults}
                onExecute={handleExecute}
                code={response.code}
                tests={response.tests}
                isExecuting={executing}
              />
            )}
          </div>
        </div>
      )}
    </div>
  )
}

export default App
