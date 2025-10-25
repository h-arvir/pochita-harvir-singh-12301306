import { useState } from 'react'
import './CodeDisplay.css'

const CodeDisplay = ({ code, language = 'python', title = 'Code', onDownload = null }) => {
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
        <div className="code-title-section">
          <h3>{title}</h3>
          <span className="code-language">Python</span>
        </div>
        <div className="code-actions">
          <button onClick={handleCopy} className={`copy-btn ${hasCopied ? 'copied' : ''}`}>
            {hasCopied ? 'Copied' : 'Copy Code'}
          </button>
          {onDownload && title === 'Generated Code' && (
            <button onClick={onDownload} className="download-btn" title="Download code as zip">
              Download Zip
            </button>
          )}
        </div>
      </div>

      <pre className="code-block">
        <code>{code}</code>
      </pre>
    </div>
  )
}

export default CodeDisplay
