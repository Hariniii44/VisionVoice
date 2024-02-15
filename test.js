const puppeteer = require('puppeteer')
const fs = require('fs/promises')

async function start() {
    const browser = await puppeteer.launch()
    const page = await browser.newPage()
    await page.goto("https://historyforkids.org/ancient-india/")

    const names = await page.evaluate(() => {
        return Array.from(document.querySelectorAll(".entry-content p")).map(x => x.textContent)
    })
    await fs.writeFile("test.txt", names.join("\r\n\n"))
    await browser.close()
}

start()
