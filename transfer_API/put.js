const { startServer } = require('./API.js');

startServer();

const axios = require('axios');

let myVariable = "new command";

axios.post('http://localhost:3000/user_command', {
  command: myVariable
})
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });