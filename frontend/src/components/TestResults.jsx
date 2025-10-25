import './TestResults.css'

export default function TestResults({ results, onExecute, code, tests, isExecuting }) {
  if (!results) {
    return null
  }

  const statusColor = results.status === 'success' ? '#22c55e' : '#ef4444'
  const statusIcon = results.status === 'success' ? '✓' : '✗'

  const handleRetry = async () => {
    if (onExecute) {
      await onExecute()
    }
  }

  return (
    <div className="test-results-container">
      <div className="test-results-header">
        <div className="header-title">
          <h2>Test Results</h2>
        </div>
        <div className="summary-badge" style={{ borderColor: statusColor }}>
          <span className="status-icon" style={{ color: statusColor }}>
            {statusIcon}
          </span>
          <span className="status-text">{results.test_summary}</span>
        </div>
      </div>

      <div className="test-stats">
        <div className="stat-box">
          <div className="stat-label">Total Tests</div>
          <div className="stat-value">{results.total_tests}</div>
        </div>
        <div className="stat-box success">
          <div className="stat-label">Passed</div>
          <div className="stat-value" style={{ color: '#22c55e' }}>
            {results.passed_tests}
          </div>
        </div>
        <div className="stat-box failed">
          <div className="stat-label">Failed</div>
          <div className="stat-value" style={{ color: '#ef4444' }}>
            {results.failed_tests}
          </div>
        </div>
      </div>

      {results.test_details && results.test_details.length > 0 && (
        <div className="test-details">
          <h3>Test Details</h3>
          <div className="test-list">
            {results.test_details.map((test, idx) => (
              <div key={idx} className={`test-item ${test.status}`}>
                <span className="test-status-icon">
                  {test.status === 'passed' ? '✓' : test.status === 'failed' ? '✗' : '⚠'}
                </span>
                <span className="test-name">{test.name}</span>
                {test.params && <span className="test-params">[{test.params}]</span>}
                <span className={`test-badge ${test.status}`}>{test.status}</span>
              </div>
            ))}
          </div>
        </div>
      )}

      {results.output && (
        <div className="test-output">
          <h3>Output</h3>
          <pre className="output-box">{results.output}</pre>
        </div>
      )}

      {results.error && (
        <div className="test-error">
          <h3>Error</h3>
          <pre className="error-box">{results.error}</pre>
        </div>
      )}

      {results.execution_status === 'timeout' && (
        <div className="timeout-alert">
          ⚠ Execution timed out. Please check your code for infinite loops or heavy computations.
        </div>
      )}

      <div className="test-actions">
        <button
          className="retry-btn"
          onClick={handleRetry}
          disabled={isExecuting}
        >
          {isExecuting ? 'Executing...' : 'Run Tests Again'}
        </button>
      </div>
    </div>
  )
}
