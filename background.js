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