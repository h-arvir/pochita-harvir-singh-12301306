import './ArchitectDisplay.css'

const ArchitectDisplay = ({ messages }) => {
  const getRoleColor = (role) => {
    switch (role) {
      case 'user':
        return 'blue'
      case 'architect':
        return 'orange'
      case 'coder':
        return 'green'
      case 'tester':
        return 'purple'
      case 'system':
        return 'gray'
      default:
        return 'gray'
    }
  }

  return (
    <div className="architect-display">
      <div className="architect-header">
        <div className="architect-title-section">
          <h3>Architecture Analysis</h3>
          <span className="architect-badge">Agent Output</span>
        </div>
      </div>

      <div className="architect-content">
        {messages && messages.length > 0 ? (
          messages.map((msg, idx) => (
            <div
              key={idx}
              className={`message message-${msg.role}`}
              style={{
                borderLeftColor: `var(--color-${getRoleColor(msg.role)})`,
              }}
            >
              <div className="message-header">
                <span className={`badge badge-${getRoleColor(msg.role)}`}>
                  {msg.role.toUpperCase()}
                </span>
                {msg.timestamp && (
                  <span className="timestamp">
                    {new Date(msg.timestamp).toLocaleTimeString()}
                  </span>
                )}
              </div>
              <div className="message-content">
                {msg.content}
              </div>
            </div>
          ))
        ) : (
          <div className="empty-state">No architecture analysis yet</div>
        )}
      </div>
    </div>
  )
}

export default ArchitectDisplay
