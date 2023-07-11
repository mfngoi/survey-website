// Retrieve elements from html document
survey_btn = document.querySelector("#a-btn");


// Add functions to run when elements are clicked
survey_btn.addEventListener("click", getAnswer);




function getAnswer() {
  let questionNum = document.getElementById("numQuestions").value;
  let question = document.getElementById("userQuestion").value;
  let endpoint = 'http://127.0.0.1:5000/chatgpt';

  // Create an object to send via POST
  let data = {
    'question': question,
    'questionNum': questionNum,
  };

  // Set the options for the request
  let options = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  };

  // Send the request
  fetch(endpoint, options);

}

/*
function getSuggestions() {
  let endpoint = 'https://api.openai.com/v1/chat/completions';

  // Create an object to send via POST
  let data = {
    'question': document.getElementById('userQuestion').value,
  };

  // Set the options for the request
  let options = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  };

  // Send the request
  fetch(endpoint, options)
  .then(response => response.json())
  .then(data => {
    document.getElementById("suggestions").style.display = "block";
    document.getElementById("suggestions").innerText = data.choices[0].message.content;
    
  })
  .catch((error) => {
    console.error('Error:', error);
  });
}
*/