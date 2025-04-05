import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [steering, setSteering] = useState(null);

  const handleDrive = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/drive', {
        sensors: [0.3, 0.7]
      });
      setSteering(response.data.steering);
    } catch (error) {
      console.error("Error calling backend:", error);
    }
  };

  return (
    <div style={{ padding: '2rem', fontFamily: 'Arial' }}>
      <h1>🧠 AI Self-Driving Car</h1>
      <button onClick={handleDrive} style={{ padding: '0.5rem 1rem' }}>
        Simulate Drive
      </button>
      {steering !== null && (
        <p style={{ marginTop: '1rem' }}>
          🚗 Steering Output: <strong>{steering}</strong>
        </p>
      )}
    </div>
  );
}

export default App;
