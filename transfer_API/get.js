const axios = require('axios');

let myVariable;

axios.get('http://localhost:3000/user_command')
  .then(response => {
    myVariable = response.data;
    console.log(myVariable);
  })
  .catch(error => {
    console.error(error);
  });