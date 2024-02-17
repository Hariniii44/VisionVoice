const puppeteer = require('puppeteer')
const fs = require('fs/promises')

async function start() {
    const browser = await puppeteer.launch()
    const page = await browser.newPage()
    let url = "https://www.oxnotes.com/ratios-igcse-maths.html"
    await page.goto(url)

    const names = await page.evaluate(() => {
        return Array.from(document.querySelectorAll("h2")).map(x => x.textContent)
    })
    await fs.writeFile("oxnotes_subsections.txt", names.join("\r\n"))
    await browser.close()
}

start()