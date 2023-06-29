const express = require('express');
const {OpenAIApi, Configuration} = require('openai');
require("dotenv").config();
const Key= process.env.key;

const axios = require("axios")
// Create an instance of the OpenAI API client

const configuration = new Configuration({
    apiKey:process.env.key
})
const openai = new OpenAIApi(configuration); // Replace 'YOUR_API_KEY' with your actual OpenAI API key

// Create an Express.js app
const app = express();

// Middleware to parse JSON requests
app.use(express.json());

// Define a route for handling the API request
app.get('/input', async (req, res) => {
  try {
    const {text}  = req.body;

    // Make a request to the OpenAI API
    const response = await openai.createCompletion({
      model: 'text-davinci-003',
      prompt: text,
      max_tokens: 100,
      temperature: 1
    });

    // Extract the generated text from the API response
    const generatedText = response.data.choices[0].text;

    // Display the generated text in the terminal
    console.log('Generated Text:', generatedText);
     res.status(200).json({
        success: true,
        data: response.data.choices[0].text,
      });
  } catch (error) {
      
    console.error('Error:', error.message);
    res.json(error)
  }
});

// Start the server
const port = process.env.port || 3000; // You can change the port number if needed
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);

  // Read input from the terminal and make API request
  const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  readline.question('Enter your request: ', (input) => {
    // Send the input as a POST request to the '/input' route
    const requestOptions = {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: input }),
    };

    axios.get('http://localhost:3000/input', { text: input})
  .then((response) => {
    console.log('Response:', response.data.result);
  })
  .catch((error) => {
    console.error('Error:', error.message);
  });
  });
});
