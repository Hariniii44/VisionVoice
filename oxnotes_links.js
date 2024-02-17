const puppeteer = require('puppeteer')
const fs = require('fs/promises')

async function start() {
    const browser = await puppeteer.launch()
    const page = await browser.newPage()
    await page.goto("https://www.oxnotes.com/igcse-mathematics.html")

    let names = await page.evaluate(() => {
        return Array.from(document.querySelectorAll(".paragraph a")).map(x => x.textContent)
    })
    names.splice(9,4)
    


    await fs.writeFile("oxnotes_links.txt", names.join("\r\n"))
    await browser.close()
}

start()
