const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(bodyParser.json());

let user_command = "some random text";

// Route to get the user command
app.get('/user_command', (req, res) => {
  res.json(user_command);
});

// Route to update the user command
app.post('/user_command', (req, res) => {
  console.log(req.body)
  let command = req.body.command;
  user_command = command;
  res.status(201).json({ message: 'User command updated successfully'});
});

// Start the server
app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});

module.exports = {
  startServer: function() {
    app.listen(port, () => {
      console.log(`Server is listening on port ${port}`);
    });
  }
};