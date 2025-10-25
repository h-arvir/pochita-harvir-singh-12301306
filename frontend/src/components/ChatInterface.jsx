import './ChatInterface.css'

const ChatInterface = ({ messages }) => {
  const getRoleColor = (role) => {
    switch (role) {
      case 'user':
        return 'blue'
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

  const getRoleEmoji = (role) => {
    switch (role) {
      case 'user':
        return '👤'
      case 'coder':
        return '💻'
      case 'tester':
        return '🧪'
      case 'system':
        return '⚙️'
      default:
        return '📝'
    }
  }

  return (
    <div className="chat-interface">
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
                {getRoleEmoji(msg.role)} {msg.role.toUpperCase()}
              </span>
              {msg.timestamp && (
                <span className="timestamp">
                  {new Date(msg.timestamp).toLocaleTimeString()}
                </span>
              )}
            </div>
            <div className="message-content">
              {msg.content.substring(0, 300)}
              {msg.content.length > 300 ? '...' : ''}
            </div>
          </div>
        ))
      ) : (
        <div className="empty-state">No messages yet</div>
      )}
    </div>
  )
}

export default ChatInterface
