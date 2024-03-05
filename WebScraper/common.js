const { execFile } = require('child_process');

execFile('node', ['oxnotes_content.js'], (error, stdout, stderr) => {
  if (error) {
    console.error(`Error executing file: ${error}`);
    return;
  }

});
