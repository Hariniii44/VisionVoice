//content.js
console.log('Content script loaded in the new tab!');
chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    console.log('Received message in content script:', request);
    if (request.action === 'triggerTTS') {
        console.log('Received triggerTTS message. Calling textToSpeech function.');
        textToSpeech('You are now in the website');
    }
});

function textToSpeech(text) {
    console.log('textToSpeech function called with text:', text);
    const utterance = new SpeechSynthesisUtterance(text);
    window.speechSynthesis.speak(utterance);
}

