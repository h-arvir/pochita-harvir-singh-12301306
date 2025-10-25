import './DocumentationDisplay.css'
import { useState } from 'react'

export default function DocumentationDisplay({ documentation, markdown }) {
  const [viewMode, setViewMode] = useState('overview')

  if (!documentation || Object.keys(documentation).length === 0) {
    return (
      <div className="documentation-container">
        <div className="empty-state">
          <p>Documentation is being generated...</p>
          <p style={{ fontSize: '12px', color: '#64748b' }}>
            If this persists, check the browser console for errors
          </p>
        </div>
      </div>
    )
  }

  const doc = documentation

  return (
    <div className="documentation-container">
      <div className="doc-header">
        <h2>Documentation</h2>
        <div className="view-mode-toggle">
          <button
            className={`toggle-btn ${viewMode === 'overview' ? 'active' : ''}`}
            onClick={() => setViewMode('overview')}
          >
            Overview
          </button>
          <button
            className={`toggle-btn ${viewMode === 'structured' ? 'active' : ''}`}
            onClick={() => setViewMode('structured')}
          >
            Detailed
          </button>
          <button
            className={`toggle-btn ${viewMode === 'markdown' ? 'active' : ''}`}
            onClick={() => setViewMode('markdown')}
          >
            Markdown
          </button>
        </div>
      </div>

      <div className="doc-content">
        {viewMode === 'overview' && (
          <div className="overview-section">
            {doc.overview && (
              <div className="section">
                <h3>Overview</h3>
                <p>{doc.overview}</p>
              </div>
            )}

            {doc.usage_examples && doc.usage_examples.length > 0 && (
              <div className="section">
                <h3>Usage Examples</h3>
                {doc.usage_examples.map((example, idx) => (
                  <div key={idx} className="example-block">
                    <h4>{example.title}</h4>
                    <p>{example.description}</p>
                    <pre className="code-block">{example.code}</pre>
                  </div>
                ))}
              </div>
            )}

            {doc.installation && (
              <div className="section">
                <h3>Installation</h3>
                {doc.installation.requirements && doc.installation.requirements.length > 0 && (
                  <>
                    <h4>Requirements</h4>
                    <ul>
                      {doc.installation.requirements.map((req, idx) => (
                        <li key={idx}>{req}</li>
                      ))}
                    </ul>
                  </>
                )}
                {doc.installation.steps && doc.installation.steps.length > 0 && (
                  <>
                    <h4>Steps</h4>
                    <ol>
                      {doc.installation.steps.map((step, idx) => (
                        <li key={idx}>{step}</li>
                      ))}
                    </ol>
                  </>
                )}
              </div>
            )}
          </div>
        )}

        {viewMode === 'structured' && (
          <div className="structured-section">
            {doc.dependencies && doc.dependencies.length > 0 && (
              <div className="section">
                <h3>Dependencies</h3>
                <div className="dependencies-grid">
                  {doc.dependencies.map((dep, idx) => (
                    <div key={idx} className="dependency-card">
                      <div className="dep-name">{dep.name}</div>
                      <div className="dep-version">v{dep.version}</div>
                      <p className="dep-description">{dep.description}</p>
                      <code className="dep-install">{dep.installation}</code>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {doc.configuration && (
              <div className="section">
                <h3>Configuration</h3>
                {doc.configuration.environment_variables && doc.configuration.environment_variables.length > 0 && (
                  <>
                    <h4>Environment Variables</h4>
                    <div className="env-vars-list">
                      {doc.configuration.environment_variables.map((envVar, idx) => (
                        <div key={idx} className="env-var">
                          <div className="env-name">
                            {envVar.name}
                            {envVar.required && <span className="required-badge">Required</span>}
                          </div>
                          <p>{envVar.description}</p>
                          {envVar.default && <div className="env-default">Default: {envVar.default}</div>}
                        </div>
                      ))}
                    </div>
                  </>
                )}
                {doc.configuration.config_file_example && (
                  <>
                    <h4>Configuration Example</h4>
                    <pre className="code-block">{doc.configuration.config_file_example}</pre>
                  </>
                )}
              </div>
            )}

            {doc.running_locally && (
              <div className="section">
                <h3>Running Locally</h3>
                {doc.running_locally.prerequisites && doc.running_locally.prerequisites.length > 0 && (
                  <>
                    <h4>Prerequisites</h4>
                    <ul>
                      {doc.running_locally.prerequisites.map((prereq, idx) => (
                        <li key={idx}>{prereq}</li>
                      ))}
                    </ul>
                  </>
                )}
                {doc.running_locally.setup_steps && doc.running_locally.setup_steps.length > 0 && (
                  <>
                    <h4>Setup Steps</h4>
                    <ol>
                      {doc.running_locally.setup_steps.map((step, idx) => (
                        <li key={idx}>{step}</li>
                      ))}
                    </ol>
                  </>
                )}
                {doc.running_locally.verification && (
                  <>
                    <h4>Verification</h4>
                    <p>{doc.running_locally.verification}</p>
                  </>
                )}
              </div>
            )}

            {doc.architecture && (
              <div className="section">
                <h3>Architecture</h3>
                {doc.architecture.description && (
                  <p>{doc.architecture.description}</p>
                )}
                {doc.architecture.ascii_diagram && (
                  <>
                    <h4>Diagram</h4>
                    <pre className="ascii-diagram">{doc.architecture.ascii_diagram}</pre>
                  </>
                )}
                {doc.architecture.components && doc.architecture.components.length > 0 && (
                  <>
                    <h4>Components</h4>
                    <div className="components-list">
                      {doc.architecture.components.map((comp, idx) => (
                        <div key={idx} className="component">
                          <div className="comp-name">{comp.name}</div>
                          <p className="comp-responsibility">{comp.responsibility}</p>
                          {comp.interactions && (
                            <p className="comp-interactions">
                              <strong>Interacts with:</strong> {comp.interactions}
                            </p>
                          )}
                        </div>
                      ))}
                    </div>
                  </>
                )}
                {doc.architecture.data_flow && (
                  <>
                    <h4>Data Flow</h4>
                    <p>{doc.architecture.data_flow}</p>
                  </>
                )}
              </div>
            )}
          </div>
        )}

        {viewMode === 'markdown' && (
          <div className="markdown-section">
            {markdown ? (
              <pre className="markdown-content">{markdown}</pre>
            ) : (
              <p>Markdown version not available</p>
            )}
          </div>
        )}
      </div>
    </div>
  )
}
