
const { createClient } = require('redis');

const puppeteer = require('puppeteer')
const fs = require('fs/promises')

const client = createClient({
    password: 'FHMAQVoWFZnH9pv47jnV6KGght8FIhL3',
    socket: {
        host: 'redis-18121.c212.ap-south-1-1.ec2.cloud.redislabs.com',
        port: 18121
    }
});

async function start() {

	try {

		const browser = await puppeteer.launch()
		const page = await browser.newPage()
		await page.goto("https://www.mathplanet.com/education/algebra-1")

		console.log("Went to the link")

		let link_names = await page.evaluate(() => {
			let l = Array.from(document.querySelectorAll("#menusubnodes a")).map(x => x.textContent)
			return l
		})


		console.log("Link names have been gotten")

		let hrefs = await page.evaluate(() => {
			let u = Array.from(document.querySelectorAll('#menusubnodes a')).map(urls => urls.href)
			return u
		})

		console.log("URLS have been gotten")

		for (let i = 0; i < link_names.length; i++){
			
			let name = 'name' + (i+1)
			client.hmSet(name, 'title', link_names[i], 'url', hrefs[i], (e, response) => {
				if (e) {
					console.log("An error ocurred")
				} else {
					console.log("Data has been set")
				}
			})

			client.expire(name, 120, (e, response) => {
				if (e){
					console.log("Error setting expiry")
				} else {
					console.log(response)
				}
			})
		}

		console.log("Set data with the URL names and URL links")

		await browser.close()

		

	} catch (e) {
		console.log("An error occurred")
	}
}

start()
client.quit()

