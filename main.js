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
            console.log(e);
            const text = Array.from(e.results)
                .map(result => result[0])
                .map(result => result.transcript)
                .join('');

            // let p = document.createElement('p');
            p.innerText = text;
            texts.appendChild(p);

            if (e.results[0].isFinal) {
                recognition.stop();    //stop recog after getting a final result
                p = document.createElement('p');
                handleResponse(text);
            }
            console.log('recognized text:', text);
        });

        recognition.addEventListener('end', ()=> {
            isRecognizing = false;
            setTimeout(() => {
                if (isRecognizing) {
                    recognition.start();
                }
            }, 500);
            // recognition.start();     //restart to keep recog continuous
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
        textToSpeech('Welcome to vision voice. which website would you like to go to?');
    }

    if (text.includes('maths is fun')) {
        replyP = createReply('opening mathsisfun');
        texts.appendChild(replyP);
        textToSpeech('Welcome to maths is fun, these are the sections you can go to in this website.');
        chrome.runtime.sendMessage({ action: 'openNewTab', url: 'https://www.mathsisfun.com/'});
        // window.open('https://www.mathsisfun.com/')
    }

    if (text.includes('aux notes') || text.includes('ox notes')) {
        replyP = createReply('opening oxnotes');
        texts.appendChild(replyP);
        textToSpeech('Welcome oxnotes, these are the sections you can go to in this website.');
        chrome.runtime.sendMessage({ action: 'openNewTab', url: 'https://www.oxnotes.com/igcse-mathematics.html'});
        // window.open('https://www.oxnotes.com/igcse-mathematics.html')
    }

    if (text.includes('mathplanet') || text.includes('math planet')) {
        replyP = createReply('opening mathplanet website');
        texts.appendChild(replyP);
        textToSpeech('Welcome mathplanet website, these are the sections you can go to in this website.');
        chrome.runtime.sendMessage({ action: 'openNewTab', url: 'https://www.mathplanet.com/'});
        // window.open('https://www.mathplanet.com/')
    }

    if (text.includes('math notes') || text.includes('mathnotes') || text.includes('maths notes')) {
        replyP = createReply('opening math notes website');
        texts.appendChild(replyP);
        textToSpeech('Welcome mathplanet website, these are the sections you can go to in this website.');
        chrome.runtime.sendMessage({ action: 'openNewTab', url: 'https://tutorial.math.lamar.edu/Classes/Alg/Alg.aspx'});
        // window.open('https://tutorial.math.lamar.edu/Classes/Alg/Alg.aspx')
    }
    startSpeechRecognition();
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

document.getElementById('startRecognitionButton').addEventListener('click', startSpeechRecognition);


