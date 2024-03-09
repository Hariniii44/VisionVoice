//content.js

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === 'startSpeechRecognition') {
        // Start speech recognition in your content script
        startSpeechRecognition();
        console.log('startSpeechRecognition');
    }
});







