import { useEffect, useRef, useState } from 'react'
import './App.css'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const EXAMPLES = [
  'What is the VPN policy?',
  'What happens if I find a vulnerability?',
  'How do I engage the security team on-call?',
  'What are the password guidelines?',
  'What is the vulnerability remediation SLA?',
]

function App() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const bottomRef = useRef(null)

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages, loading])

  async function sendMessage(text) {
    const question = text.trim()
    if (!question || loading) return

    setError(null)
    setInput('')
    setMessages((prev) => [...prev, { role: 'user', content: question }])
    setLoading(true)

    try {
      const res = await fetch(`${API_URL}/api/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: question }),
      })

      if (!res.ok) {
        throw new Error(`Request failed (${res.status})`)
      }

      const data = await res.json()
      setMessages((prev) => [
        ...prev,
        { role: 'assistant', content: data.answer, sources: data.sources },
      ])
    } catch (err) {
      setError(err.message || 'Something went wrong')
    } finally {
      setLoading(false)
    }
  }

  function handleSubmit(e) {
    e.preventDefault()
    sendMessage(input)
  }

  return (
    <div className="app">
      <header className="header">
        <h1>Security Handbook Assistant</h1>
        <p>Ask questions about GitLab's security policies and handbook. Powered by RAG + Knowledge Graph.</p>
      </header>

      <main className="chat">
        {messages.length === 0 && (
          <div className="examples">
            {EXAMPLES.map((example) => (
              <button key={example} type="button" onClick={() => sendMessage(example)}>
                {example}
              </button>
            ))}
          </div>
        )}

        {messages.map((msg, i) => (
          <div key={i} className={`message ${msg.role}`}>
            <div className="bubble">
              <p>{msg.content}</p>
              {msg.sources && msg.sources.length > 0 && (
                <details className="sources">
                  <summary>Sources ({msg.sources.length})</summary>
                  <ul>
                    {msg.sources.map((s, j) => (
                      <li key={j}>
                        <a href={s.url} target="_blank" rel="noreferrer">
                          {s.breadcrumb}
                        </a>
                      </li>
                    ))}
                  </ul>
                </details>
              )}
            </div>
          </div>
        ))}

        {loading && (
          <div className="message assistant">
            <div className="bubble typing">
              <span></span>
              <span></span>
              <span></span>
            </div>
          </div>
        )}

        {error && <div className="error">{error}</div>}

        <div ref={bottomRef} />
      </main>

      <form className="composer" onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Ask a security question..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          disabled={loading}
        />
        <button type="submit" disabled={loading || !input.trim()}>
          Send
        </button>
      </form>
    </div>
  )
}

export default App
