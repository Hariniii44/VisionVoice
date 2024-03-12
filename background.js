//background.js

let shouldReadContent = false;
let currentSection = '';

// Function to open the extension window
function openExtensionWindow() {
    chrome.windows.create({
        url: 'index.html',
        type: 'popup',
        width: 400, 
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

//open extension window if it's not open on startup
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

            chrome.tabs.onUpdated.addListener(function (updatedTabId, changeInfo, updatedTab) {
                if (changeInfo.status === 'complete' && updatedTabId === tab.id) {
                    console.log('tab is updated');
                    chrome.tabs.sendMessage(tab.id, { action: 'tabUpdated', url: request.url }, function(response) {
                        console.log('Message sent to content script');
                    });
                }
            });
        });
    }
});






