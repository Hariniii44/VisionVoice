// Import the scraping script
const { start, emptyFolder } = require('./oxnotes_content.js');

// Define the folder destination
const folderDestination = "../Images";

module.exports.emptyFolder = emptyFolder;
// Call the function to empty the folder
emptyFolder(folderDestination)
  .then(() => {
    // Call the function to start scraping
    start();
  })
  .catch(error => {
    console.error('An error occurred while emptying the folder:', error);
  });
