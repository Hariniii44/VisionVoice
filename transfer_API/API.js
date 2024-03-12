const express = require('express');
const bodyParser = require('body-parser');

const api = express();
const port = 3000;

// Middleware to parse JSON bodies
api.use(bodyParser.json());

let user_command = "";

// Route to get the user command
api.get('/user_command', (req, res) => {
  res.json(user_command);
});

// Route to update the user command
api.post('/user_command', (req, res) => {
  const command = req.body.command;
  user_command = command;
  res.status(201).json({ message: 'User command updated successfully' });
});

// Start the server
api.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});

module.exports = {
  startServer: function() {
    api.listen(port, () => {
      console.log(`Server is listening on port ${port}`);
    });
  }
};