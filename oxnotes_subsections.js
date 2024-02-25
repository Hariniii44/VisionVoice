const puppeteer = require('puppeteer')
const fs = require('fs/promises')
const ds = require('fs')

let fileName = "oxnotes_subsections.txt"

async function start() {

	ds.access(fileName, ds.constants.F_OK, (e) => {
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
	const page = await browser.newPage()
	await page.goto("https://www.oxnotes.com/ratios-igcse-maths.html")

	const names = await page.evaluate(() => {
		return Array.from(document.querySelectorAll("h2")).map(x => x.textContent)
	})
	await fs.writeFile(fileName, names.join("\r\n"))
	console.log('Wrote to text file');
	await browser.close()
}

start()