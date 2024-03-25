// const { startServer } = require('./API.js');

// startServer();

const axios = require('axios');

let myVariable = "";

axios.post('http://localhost:3000/user_command', {
  data: myVariable
})
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });