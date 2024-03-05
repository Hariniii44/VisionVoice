const puppeteer = require('puppeteer')
//provides access to puppeteer
const fs = require('fs/promises')
//this import provides the asynchronous version of the file system functions
const ds = require('fs')
//this import provides the synchronous version of the file system functions
const path = require('path')
//imports the path module

let fileName = "../Text_com/content.txt"
//specifies the output text file

let url = "https://www.mathsisfun.com/algebra/polynomials-dividing.html"
//gives the url that is to be navigated to
const folderDestination = "../Images"
//specifies the folder destination


async function emptyFolder(folderLocation) { //an asnyc function (allowing us to use the await function) to empty the images folder of any previous old images
    try {
        let files = await fs.readdir(folderLocation)

		//read the contents of the folder

        for (let file of files) { //iterate over each file in the folder
            let filePath = path.join(folderLocation, file)//get the full path of the file

			await fs.unlink(filePath)//deletes the file

        }

        console.log("Emptied Images folder")
        //logs to let you know that the folder was emptied
    } catch (error) {
        console.error("An error occurred while emptying the folder")
    }
}


async function start() {
	try {
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
		await page.goto(url)
	//a new page is created which goes to the specified URL
		const names = await page.evaluate(() => {
			return Array.from(document.querySelectorAll("p")).map(x => x.textContent)
			//the textcontent from the specific CSS selector (to the webpage) is selected and returned as an array
		})
		await fs.writeFile(fileName, names.join("\r\n"))
		//the array is written to a file with each member written to one line
		console.log('Wrote to text file');

		// Get the URLs of the images in the specified CSS selector
        const photoUrls = await page.$$eval("#content img", imgs => {
            return imgs.map(x => x.src)
        })

		// Download the specific images from the css selectors
        for (const [index, photoUrl] of photoUrls.entries()) {//iterates with the index and url of the photoUrls array
            const imagePage = await page.goto(photoUrl)//goes to the image page of the URL
            const imageBuffer = await imagePage.buffer() //awaits the image buffer
            const imageName = `${index + 1}_${photoUrl.split("/").pop()}` // Add index to be neat
            const imagePath = `${folderDestination}/${imageName}`//create the file path of the image
            await fs.writeFile(imagePath, imageBuffer)//writes the file to the path
            console.log(`Downloaded:  ${index + 1} of ${photoUrls.length}`)//logs to show the progress
        }

        console.log('Downloaded all the images to the Images folder, if there were any') //Logs to show the process is complete
	
		await browser.close()
		//the console logs that the file has been written to and the headless browser is closed
	}
	catch (error){
		console.error("An error occurred with the start() process")
	}

}

emptyFolder(folderDestination)
//the folder is emptied first

start()
//the async function start() is called when this file is run