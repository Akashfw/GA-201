const express = require('express');
const {OpenAIApi, Configuration} = require('openai');
require("dotenv").config();

// Create an instance of the OpenAI API client

const configuration = new Configuration({
    apiKey:process.env.key
})
const openai = new OpenAIApi(configuration); // Replace 'YOUR_API_KEY' with your actual OpenAI API key

// Create an Express.js app
const app = express();
const cors= require("cors")
// Middleware to parse JSON requests
app.use(cors());
app.use(express.json());

// Define a route for generating Shayari
app.post('/input', async (req, res) => {
  try {
    const { topic } = req.body;

    // Make a request to the OpenAI API
    const response = await openai.createCompletion({
      model: 'text-davinci-003',
      prompt: `write a Shayari on ${topic}`,
      max_tokens: 250,
      temperature: 0.7,
      n: 1
    });
      

    // Extract the generated Shayari from the API response
    const generatedShayari = response.data.choices[0].text.trim();

    // Return the generated Shayari as the API response
    res.json({ shayari: generatedShayari });
  } catch (error) {
    console.error('Error:', error.message);
    res.status(500).json({ error: 'An error occurred' });
  }
});

// Start the server
const port = 3000; // You can change the port number if needed
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
