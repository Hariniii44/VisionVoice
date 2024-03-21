const express = require('express');
const bodyParser = require('body-parser');
// const { exec } = require('child_process');

const api = express();
const port = 3000;

const WebSocket = require('ws');

const webSocket = new WebSocket.Server({ port: 8080 });
//creates a websocket

// Middleware to parse JSON bodies
api.use(bodyParser.json());

let user_command = "command";
let url = "sample url";
let sub_links = ["",""];
let content = "sample content"


// Route to get the content
api.get('/content', (_, res) => {
  res.json(content);
});

webSocket.on('connection', ws => {
  // this is done that when content is updated there will be a notification to background.js
  api.post('/content', (req, res) => {
    let newContent = req.body.content;
    content = newContent;
    ws.send('contentUpdated');
    res.json({ message: 'Content updated successfully' });
  });
});


// Route to get the sub links
api.get('/sub_links', (_, res) => {
  res.json(sub_links);
});

// Route to update the sub links
api.post('/sub_links', (req, res) => {
  console.log(req.body)
  let newSubLinks = req.body.sub_links;
  sub_links = newSubLinks;
  res.json({ message: 'Sub links updated successfully' });
});

// function sendURLToExtension(url) {
//   chrome.runtime.sendMessage( 'onlnadlphenfaabogkleohajhoidjkjg', { type: 'url_from_node', url: url });
// }

// Route to get the url
api.get('/url', (_, res) => {
  res.json(url);
});

// Route to update the url
api.post('/url', (req, res) => {
  console.log(req.body)
  let new_url = req.body.url;
  url = new_url;
   res.json({ message: 'URL updated successfully' });
});

  // Execute the Python script using child_process.exec
//   exec('python NLP/new_commands.py', (error, stdout, stderr) => {
//     if (error) {
//       console.error(`exec error: ${error}`);
//       // res.status(500).json({ error: 'Error executing Python script' });
//       return;
//     }
//     console.log(`stdout: ${stdout}`);
//     console.error(`stderr: ${stderr}`);

//     const currentURL = stdout.trim();
//     console.log(`URL: ${currentURL}`);
    
//     if (currentURL) {
//       sendURLToExtension(currentURL);
//     }
//     // res.status(201).json({ message: 'URL updated successfully'}); 
//   });
// });

// Route to get the user command
api.get('/user_command', (_, res) => {
  res.json(user_command);
});

// Route to update the user command
api.post('/user_command', (req, res) => {
  console.log(req.body)
  let command = req.body.user_command;
  user_command = command;
  res.status(201).json({ message: 'User command updated successfully'});
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