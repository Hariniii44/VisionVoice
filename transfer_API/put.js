// const { startServer } = require('./API.js');

// startServer();

const axios = require('axios');

let myVariable = "Warhammer 40k!!!";

axios.post('http://localhost:3000/user_command', {
  data: myVariable
})
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });