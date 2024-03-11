const slider = document.getElementById("myrange");
const output = document.getElementById("slider-value");
const texts = document.querySelector('.texts');
// const recognition  = new webkitSpeechRecognition();
let recognition;
let isRecognizing = false;
let shouldReadContent = false;
let sectionCount = 0;
goToSectionBoolean = false;


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
                .map(result => result.transcript.toLowerCase())
                .join('');

            p.innerText = text.toLowerCase(); 
            texts.appendChild(p);

            if (e.results[0].isFinal) {
                p = document.createElement('p');
                handleResponse(text.toLowerCase()); // pass lowercase text to handleResponse function
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
        textToSpeech('Welcome to vision voice. which website would you like to go to? ');   //You can either go to maths is fun, oxnotes, mathplanet or pauls online notes
    }
    else if (text.includes('maths is fun')) {
        replyP = createReply('opening mathsisfun');
        texts.appendChild(replyP);
        textToSpeech('Welcome to maths is fun.');  //these are the sections you can go to in this website. The Basics, Exponents , Simplifying, Factoring, Logarithms, Polynomials, Linear Equations, Quadratic Equations, Solving Word Questions, Functions, Sequences and Series
        chrome.runtime.sendMessage({ action: 'openNewTab', url: 'https://www.mathsisfun.com/algebra/index.html'});
    }
    else if (text.includes('aux notes') || text.includes('Ox notes') || text.includes('ox notes')) {
        replyP = createReply('opening oxnotes');
        texts.appendChild(replyP);
        textToSpeech('Welcome to oxnotes, these are the sections you can go to in this website.');
        chrome.runtime.sendMessage({ action: 'openNewTab', url: 'https://www.oxnotes.com/igcse-mathematics.html'});
    }
    else if (text.includes('mathplanet') || text.includes('math planet')) {
        replyP = createReply('opening mathplanet website');
        texts.appendChild(replyP);
        textToSpeech('Welcome to mathplanet website, these are the sections you can go to in this website.');
        chrome.runtime.sendMessage({ action: 'openNewTab', url: 'https://www.mathplanet.com/education/algebra-2'});
    }
    else if (text.includes('online notes') || text.includes('pauls online notes') || text.includes('paulsonlinenotes')) {
        replyP = createReply('opening pauls online notes website');
        texts.appendChild(replyP);
        textToSpeech('Welcome to pauls online notes, these are the sections you can go to in this website.');
        chrome.runtime.sendMessage({ action: 'openNewTab', url: 'https://tutorial.math.lamar.edu/Classes/Alg/Alg.aspx'});
    }    
    if (text.includes('the basics') || text.includes('exponents') || text.includes('simplifying') || text.includes('factoring') || text.includes('logarithms') || text.includes('polynomials') || text.includes('linear equations') || text.includes('quadratic equations') || text.includes('solving word questions') || text.includes('functions') || text.includes('sequences and series')) {
        if (goToSectionBoolean) {
            goToSection(text);
        } else {
            const userInput = text.toLowerCase(); 
            // assign userInput to a variable
            console.log('User Input:', userInput);
        }
    } else {
        const userInput = text.toLowerCase(); 
        // assign userInput to a variable
        console.log('User Input:', userInput);
    }
}



function goToSection(text) {
    const section = extractSection(text);
    console.log(section);
    if (isValidSection(section)) {
        let content = '';
        if (section === 'the basics') {
            content = 'This is the content for The Basics section.';
        } else if (section === 'exponents') {
            content = 'This is the content for Exponents section.';
        } else if (section === 'simplifying') {
            content = 'This is the content for Simplifying section.';
        } else if (section === 'factoring') {
            content = 'This is the content for Factoring section.';
        } else if (section === 'logarithms') {
            content = 'This is the content for Logarithms section.';
        } else if (section === 'polynomials') {
            content = 'This is the content for Polynomials section.';
        } else if (section === 'linear equations') {
            content = 'This is the content for Linear Equations section.';
        } else if (section === 'quadratic equations') {
            content = 'This is the content for Quadratic Equations section.';
        } else if (section === 'solving word questions') {
            content = 'This is the content for Solving Word Questions section.';
        } else if (section === 'functions') {
            content = 'This is the content for Functions section.';
        } else if (section === 'sequences and series') {
            content = 'This is the content for Sequences and Series section.';
        }

        textToSpeech(content , () => {
            sectionCount++;
            console.log(`Section "${section}" identified ${sectionCount} times.`);

            if (sectionCount >= 1) {
                return; // Terminate the function
            }            
        });
    } else {
        textToSpeech('Invalid section mentioned. Please try again.');
        console.log('Invalid section mentioned:', section);
    }
}

function extractSection(text) {
    //extract the section from the command
    const match = text.match(/go to (\b(?:the basics|exponents|simplifying|factoring|logarithms|polynomials|linear equations|quadratic equations|solving word questions|functions|sequences and series)\b)/i);
    return match ? match[1] : ''; // Return the captured section
}

function isValidSection(section) {
    //check if the extracted section is valid
    const validSections = ['the basics', 'exponents', 'simplifying', 'factoring', 'logarithms', 'polynomials', 'linear equations', 'quadratic equations', 'solving word questions', 'functions', 'sequences and series'];
    return validSections.includes(section);
}

function createReply(replyText) {
    let replyP = document.createElement('p');
    replyP.classList.add('reply');
    replyP.innerText = replyText;
    return replyP;
}

function textToSpeech(text, callback) {
    if (recognition && isRecognizing) {
        recognition.stop();
        isRecognizing = false;
    }
    
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.onend = function() {
        if (callback && typeof callback === 'function') {
            callback();
        }
        if (recognition) {
            recognition.start();
            isRecognizing = true;
        }
    };
    window.speechSynthesis.speak(utterance);
}

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === 'startSpeechRecognition') {
        const url = request.url; // get the url from the message
        console.log('Received URL:', url);
        startSpeechRecognition();
    }
    if (request.action === 'goToSection') {
        goToSectionBoolean = true;
    }
});

startSpeechRecognition(); //start when the window is opened

console.log(extractSection('go to the basics')); // Output: "The Basics"
console.log(extractSection('Go To Exponents')); // Output: "Exponents"
console.log(extractSection('Go to Linear Equations')); // Output: "Linear Equations"
console.log(isValidSection('The Basics')); // Output: true
console.log(isValidSection('Algebra')); // Output: false


