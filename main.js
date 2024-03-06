const slider = document.getElementById("myrange");
const output = document.getElementById("slider-value");
const texts = document.querySelector('.texts');
// const recognition  = new webkitSpeechRecognition();
let recognition;
let isRecognizing = false;

    output.innerHTML = slider.value;

    slider.oninput = function() {
        output.innerHTML = this.value;
    }


function startSpeechRecognition() {
    texts.innerHTML = '';    //clear previous
    if (!recognition || !isRecognizing) {
        recognition  = new webkitSpeechRecognition();
        recognition.interimResults = true;
        let p = document.createElement('p');

        recognition.addEventListener('result', (e) => {
            // console.log(e);
            const text = Array.from(e.results)
                .map(result => result[0])
                .map(result => result.transcript)
                .join('');

            p.innerText = text;
            texts.appendChild(p);

            if (e.results[0].isFinal) {
                p = document.createElement('p');
                handleResponse(text);
            }
        });

        recognition.addEventListener('end', ()=> {
            // isRecognizing = false;
            if (isRecognizing) {
                setTimeout(() => {
                    recognition.start();
                }, 100);
            }
        });

        isRecognizing = true;
        recognition.start();
    }
}

function handleResponse(text) {
    let replyP;

    if (text.includes('hello')) {
        replyP = createReply('Hi');
        texts.appendChild(replyP);
        textToSpeech('Welcome to vision voice. which website would you like to go to? You can either go to maths is fun, oxnotes, mathplanet or pauls online notes');
    }
    else if (text.includes('maths is fun')) {
        replyP = createReply('opening mathsisfun');
        texts.appendChild(replyP);
        textToSpeech('Welcome to maths is fun, these are the sections you can go to in this website.');
        chrome.runtime.sendMessage({ action: 'openNewTab', url: 'https://www.mathsisfun.com/algebra/index.html'});
    }
    else if (text.includes('aux notes') || text.includes('ox notes')) {
        replyP = createReply('opening oxnotes');
        texts.appendChild(replyP);
        textToSpeech('Welcome to oxnotes, these are the sections you can go to in this website.');
        chrome.runtime.sendMessage({ action: 'openNewTab', url: 'https://www.oxnotes.com/igcse-mathematics.html'});
        // window.open('https://www.oxnotes.com/igcse-mathematics.html')
    }
    else if (text.includes('mathplanet') || text.includes('math planet')) {
        replyP = createReply('opening mathplanet website');
        texts.appendChild(replyP);
        textToSpeech('Welcome to mathplanet website, these are the sections you can go to in this website.');
        chrome.runtime.sendMessage({ action: 'openNewTab', url: 'https://www.mathplanet.com/'});
        // window.open('https://www.mathplanet.com/')
    }
    else if (text.includes('online notes') || text.includes('pauls online notes') || text.includes('paulsonlinenotes')) {
        replyP = createReply('opening math notes website');
        texts.appendChild(replyP);
        textToSpeech('Welcome to pauls online notes, these are the sections you can go to in this website.');
        chrome.runtime.sendMessage({ action: 'openNewTab', url: 'https://tutorial.math.lamar.edu/Classes/Alg/Alg.aspx'});
        // window.open('https://tutorial.math.lamar.edu/Classes/Alg/Alg.aspx')
    }
    else if (text.includes('go to')) {
        // Extract the section from the command
        const section = extractSection(text);

        if (isValidSection(section)) {
            // Send a message to background.js to handle navigation
            chrome.runtime.sendMessage({ action: 'navigateToSection', section: section });
        } else {
            // Handle invalid section
            console.log('Invalid section mentioned:', section);
        }            
    }
    else {
        textToSpeech('Your voice command is not clear. Please repeat.');
    }
}

function createReply(replyText) {
    let replyP = document.createElement('p');
    replyP.classList.add('reply');
    replyP.innerText = replyText;
    return replyP;
}

function textToSpeech(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    window.speechSynthesis.speak(utterance);
}

function extractSection(text) {
    // Implement logic to extract the section from the command

    // You might use regular expressions or other methods depending on your use case
    // For simplicity, let's assume the command structure is "go to [section]"
    // const match = text.match(/go to (.+)/i);
    const match = text.match(/go to (\b(?:The Basics|Exponents|Simplifying|Factoring|Logarithms|Polynomials|Linear Equations)\b)/i);
    return match ? match[1] : ''; // Return the captured section
}

function isValidSection(section) {
    // Add logic to check if the extracted section is valid
    // You might want to compare it against a list of valid sections
    const validSections = ['The Basics', 'Exponents', 'Simplifying', 'Factoring', 'Logarithms', 'Polynomials', 'Linear Equations'];
    return validSections.includes(section);
}

startSpeechRecognition(); //start when the window is opened

// document.getElementById('startRecognitionButton').addEventListener('click', startSpeechRecognition);


