//background.js

// Function to open the extension window
function openExtensionWindow() {
    chrome.windows.create({
        url: 'index.html',
        type: 'popup',
        width: 400, // Adjust width and height as needed
        height: 800
    }, function (window) {
        chrome.tabs.onUpdated.addListener(function onTabUpdated(tabId, changeInfo, updatedTab) {
            if (tabId === window.tabs[0].id && changeInfo.status === 'complete') {
                // Start speech recognition when the extension window is fully loaded
                // startSpeechRecognition();
                chrome.tabs.onUpdated.removeListener(onTabUpdated);
            }
        });
    });
}

// Open the extension window when the extension is first installed or updated
chrome.runtime.onInstalled.addListener(function() {
    openExtensionWindow();
});

// Additional listener to open extension window if it's not open on startup
chrome.runtime.onStartup.addListener(function() {
    chrome.windows.getAll({ populate: true }, function(windows) {
        let isExtensionWindowOpen = false;
        for (let i = 0; i < windows.length; i++) {
            if (windows[i].tabs && windows[i].tabs[0].url.includes('index.html')) {
                isExtensionWindowOpen = true;
                break;
            }
        }
        // If extension window is not open, open it
        if (!isExtensionWindowOpen) {
            openExtensionWindow();
        }
    });
});

//opening the tab
chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.action === 'openNewTab') {
        chrome.tabs.create({ url: request.url}, function(tab) {
            console.log('new tab is created', tab.id);

            //detect when the new website is fully loaded.
            chrome.tabs.onUpdated.addListener(function onTabUpdated(tabId, changeInfo, updatedTab) {
            // function onTabUpdated(tabId, changeInfo, updatedTab) {
                if (tabId === tab.id && changeInfo.status === 'complete')  {
                    console.log('tab loaded, triggering tts');
                    //if fully loaded, trigger tts
                    chrome.tabs.sendMessage(tab.id, { action: 'triggerTTS'});
                    chrome.tabs.onUpdated.removeListener(onTabUpdated);
                }  
            });
        });
    }
});

chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.action === 'navigateToSection') {
        handleNavigationCommand(request.section);
    }
})

function handleNavigationCommand(section) {
    // Perform actions based on the recognized command
    switch (section.toLowerCase()) {
        case 'the basics':
            // Logic to navigate to 'The Basics' section
            openSectionUrl('https://www.mathsisfun.com/algebra/introduction.html');
            break;
        case 'exponents':
            // Logic to navigate to 'Exponents' section
            openSectionUrl('https://example.com/exponents');
            break;
        case 'simplifying':
            // Logic to navigate to 'Simplifying' section
            openSectionUrl('https://example.com/simplifying');
            break;
        case 'factoring':
            // Logic to navigate to 'Factoring' section
            openSectionUrl('https://example.com/factoring');
            break;
        case 'logarithms':
            // Logic to navigate to 'Logarithms' section
            openSectionUrl('https://example.com/logarithms');
            break;
        case 'polynomials':
            // Logic to navigate to 'Polynomials' section
            openSectionUrl('https://example.com/polynomials');
            break;
        case 'linear equations':
            // Logic to navigate to 'Linear Equations' section
            openSectionUrl('https://example.com/linear-equations');
            break;
        default:
            // Handle unrecognized command
            console.log('Unrecognized section:', section);
            break;
    }
}

function openSectionUrl(url) {
    // Implement logic to open the specified URL
    chrome.tabs.create({ url: url }, function(tab) {
        // Additional logic if needed after opening the section URL
    });
}