// node --version # Should be >= 18
// npm install @google/generative-ai

const {
    GoogleGenerativeAI,
    HarmCategory,
    HarmBlockThreshold,
  } = require("@google/generative-ai");
  
  const MODEL_NAME = "gemini-pro";
  const API_KEY = "AIzaSyDdjzJ8VmKnfHhcINX0nwLepnPEPUkA2u8";
  
  async function run() {
    const genAI = new GoogleGenerativeAI(API_KEY);
    const model = genAI.getGenerativeModel({ model: MODEL_NAME });
  
    const generationConfig = {
      temperature: 0.9,
      topK: 1,
      topP: 1,
      maxOutputTokens: 2048,
    };
  
    const safetySettings = [
      {
        category: HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold: HarmBlockThreshold.BLOCK_ONLY_HIGH,
      },
      {
        category: HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold: HarmBlockThreshold.BLOCK_ONLY_HIGH,
      },
      {
        category: HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold: HarmBlockThreshold.BLOCK_ONLY_HIGH,
      },
      {
        category: HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold: HarmBlockThreshold.BLOCK_ONLY_HIGH,
      },
    ];

    const fs = require('fs');

    
    let filePath = 'alan_wake.txt';

    let fileContent = "";
    
    
    fs.readFile(filePath, 'utf-8', async (err, data) => {
      if (err) {
        console.error('Error reading the file:', err);
        return;
      }
      
      fileContent = data;

      let paragraph = fileContent;

      let text1 = "Explain the following text in a simple and concise manner, '" + paragraph + "'";

      const parts = [
        {text: text1},
      ];
    
      let result = await model.generateContent({
        contents: [{ role: "user", parts }],
        generationConfig,
        safetySettings,
      });
    
      let response = result.response;

      let textToWrite = response.text();

      let filePath2 = "summarized_content.txt";

      fs.writeFile(filePath2, textToWrite, 'utf-8', (err) => {
        if (err) {
          console.error('Error writing to the file:', err);
          return;
        }
        console.log('Successfully wrote to the file:', filePath2);
      });
      
    });
    
  }
  
  run();