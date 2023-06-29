const API_KEY = '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'; // Replace 'YOUR_API_KEY' with your actual API key
function generateShayari() {
  const topicInput = document.getElementById('topicInput');
  const shayariResponse = document.getElementById('shayariResponse');

  // Send a POST request to the server
  fetch('http://localhost:3000/input', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${API_KEY}`
    },
    body: JSON.stringify({ topic: topicInput.value })
  })
  .then(response => response.json())
  .then(data => {
    shayariResponse.textContent = data.shayari;
  })
  .catch(error => {
    console.error('Error:', error.message);
  });
}

  