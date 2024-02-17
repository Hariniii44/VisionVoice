const puppeteer = require('puppeteer')
const fs = require('fs/promises')

async function start() {
    const browser = await puppeteer.launch()
    const page = await browser.newPage()
    let url = "https://www.oxnotes.com/ratios-igcse-maths.html"
    await page.goto(url)

    let names = await page.evaluate(() => {
        return Array.from(document.querySelectorAll(".paragraph")).map(x => x.textContent)
    })
    names.splice(0,1)
    names.splice(names.length - 1,1)
    await fs.writeFile("content.txt", names.join("\r\n"))
    await browser.close()
}

start()