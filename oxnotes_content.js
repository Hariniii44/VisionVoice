const puppeteer = require('puppeteer')
//provides access to puppeteer
const fs = require('fs/promises')
//this import provides the asynchronous version of the file system functions
const ds = require('fs')
//this import provides the synchronous version of the file system functions

let fileName = "content.txt"
//specifies the output text file

async function start() {
//the beginning of the async function start, allowing the await function to be called
	ds.access(fileName, ds.constants.F_OK, (e) => {
		//this function checks and logs if the above file exists or not
		if (e) {
			console.error('File does not exist');
		} else {
			ds.unlink(fileName, (e) => {
				if (e) {
					console.error('An error occurred');
				} else {
					console.error('File has been deleted');
				}
			});
		}
	});

	const browser = await puppeteer.launch()
	//the browser is launched
	const page = await browser.newPage()
	await page.goto("https://www.oxnotes.com/bounds-igcse-maths.html")
//a new page is created which goes to the specified URL
	const names = await page.evaluate(() => {
		return Array.from(document.querySelectorAll(".paragraph")).map(x => x.textContent)
		//the textcontent from the specific CSS selector (to the webpage) is selected and returned as an array
	})

  await fs.writeFile(fileName, names.join("\r\n"))
  //the array is written to a file with each member written to one line
  console.log('Wrote to text file');
  await browser.close()
  //the console logs that the file has been written to and the headless browser is closed
}

start()
//the async function start() is called when this file is run