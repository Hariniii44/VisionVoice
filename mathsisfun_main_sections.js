const puppeteer = require('puppeteer')
const fs = require('fs/promises')

async function start() {
    const browser = await puppeteer.launch()
    const page = await browser.newPage()
    await page.goto("https://www.mathsisfun.com/algebra/index.html")

    const names = await page.evaluate(() => {
        return Array.from(document.querySelectorAll("h2")).map(x => x.textContent)
    })
    await fs.writeFile("mathsisfun_main_sections.txt", names.join("\r\n"))
    await browser.close()
}

start()