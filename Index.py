import React, { useState } from 'react';
import './App.css';

function App() {
  const [inputText, setInputText] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!inputText.trim()) return;

    setLoading(true);
    setResult(null);

    try {
      const response = await fetch('http://localhost:5000/api/detect', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: inputText })
      });

      const data = await response.json();
      setResult(data);
    } catch (error) {
      setResult({ error: 'An error occurred. Please try again.' });
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <h1>🕵️ Exposing the Truth</h1>
      <p>Enter an article or news excerpt to detect whether it's fake or real using NLP.</p>
      <textarea
        placeholder="Paste news article here..."
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
      />
      <button onClick={handleSubmit} disabled={loading}>
        {loading ? 'Analyzing...' : 'Check Authenticity'}
      </button>

      {result && (
        <div className="result">
          {result.error ? (
            <p className="error">{result.error}</p>
          ) : (
            <p className={result.label === 'FAKE' ? 'fake' : 'real'}>
              This news is likely: <strong>{result.label}</strong>
            </p>
          )}
        </div>
      )}
    </div>
  );
}

export default App;
