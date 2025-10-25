import { useState } from 'react'
import './CodeDisplay.css'

const CodeDisplay = ({ code, language = 'python', title = 'Code' }) => {
  const [hasCopied, setHasCopied] = useState(false)

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(code)
      setHasCopied(true)
      setTimeout(() => setHasCopied(false), 2000)
    } catch (err) {
      console.error('Failed to copy:', err)
    }
  }

  return (
    <div className="code-display">
      <div className="code-header">
        <h3>{title}</h3>
        <button onClick={handleCopy} className="copy-btn">
          {hasCopied ? '✓ Copied!' : '📋 Copy'}
        </button>
      </div>

      <pre className="code-block">
        <code>{code}</code>
      </pre>
    </div>
  )
}

export default CodeDisplay
