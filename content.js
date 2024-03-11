//content.js
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === 'tabUpdated') {
        const updatedUrl = request.url;    //url of the cirrent website
        console.log('Received tabUpdated message:', updatedUrl);

        // Identify the website based on the updatedUrl
        if (updatedUrl.includes('mathplanet.com')) {
            console.log('mathplanet website was opened');
            // Call mathplanet_links.js file to execute it
            const script = document.createElement('script');
            script.src = 'webscraper/mathplanet_links.js';
            document.head.appendChild(script);
        } else if (updatedUrl.includes('tutorial.math.lamar.edu')) {
            console.log('Pauls online notes website was opened');
            // Call paul_links.js file to execute it    
            const script = document.createElement('script');
            script.src = 'webscraper/paul_links.js';
            document.head.appendChild(script);
        } else if (updatedUrl.includes('oxnotes.com')) {
            console.log('Oxnotes website was opened');
            const script = document.createElement('script');
            script.src = 'webscraper/oxnotes_links.js';
            document.head.appendChild(script);
        } else if (updatedUrl.includes('mathsisfun.com')) {
            console.log('mathsisfun website was opened');
            chrome.runtime.sendMessage({ action: 'goToSection' });
        } else {
            console.log('Unknown website was opened');
        }
        

        //implement TTS to read the content from the webscraper


    }
});






