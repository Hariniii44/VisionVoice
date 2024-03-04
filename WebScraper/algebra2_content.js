const puppeteer = require('puppeteer')
const fs = require('fs').promises
const path = require('path')

const fileName = "content.txt"
const folderDestination = "../Images"// Specify the folder for downloaded images

async function emptyFolder(folderLocation) {
    try {
        let files = await fs.readdir(folderLocation)

		//read the contents of the folder

        for (let file of files) { //iterate over each file in the folder
            let filePath = path.join(folderLocation, file)//get the full path of the file

			await fs.unlink(filePath)//deletes the file

        }

        console.log("Emptied Images folder")
    } catch (error) {
        console.error("An error occurred while emptying the folder")
    }
}

async function start() {
    try {

        // Check if the file exists and delete it if it does
        const fileExists = await fs.access(fileName)
            .then(() => true)
            .catch(() => false);

        if (fileExists) {
            // Delete the file if it exists
            await fs.unlink(fileName);
            console.error('The old file has been deleted')
        } else {
            console.log('The file is not there')
        }

        const browser = await puppeteer.launch()
        const page = await browser.newPage()
        await page.goto("https://www.mathplanet.com/education/algebra-2/exponential-and-logarithmic-functions/exponential-functions")

        // Extract text content from paragraphs
        const names = await page.evaluate(() => {
            return Array.from(document.querySelectorAll(".body p")).map(x => x.textContent)
        })

        // Write text content to file
        await fs.writeFile(fileName, names.join("\r\n"))
        console.log('Wrote text content to file')

        // Extract image URLs
        const photoUrls = await page.$$eval(".body img", imgs => {
            return imgs.map(x => x.src)
        })

        // Create the folder for downloaded images if it doesn't exist
        await fs.mkdir(folderDestination, { recursive: true })

        // Download the specific images from the css selectors
        for (const [index, photoUrl] of photoUrls.entries()) {
            const imagePage = await page.goto(photoUrl)
            const imageBuffer = await imagePage.buffer()
            const imageName = `${index + 1}_${photoUrl.split("/").pop()}` // Add index to be neat
            const imagePath = `${folderDestination}/${imageName}`
            await fs.writeFile(imagePath, imageBuffer)
            console.log(`Downloaded:  ${imageName}`)
        }

        console.log('Wrote images to folder:', folderDestination);
        await browser.close() // Close the browser 
    } catch (error) {
        console.error('An error occurred:', error)
    }
}

emptyFolder(folderDestination)

start()

