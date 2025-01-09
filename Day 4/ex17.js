// from https://www.freecodecamp.org/news/make-api-calls-in-javascript/

// Define the API URL
const apiUrl = 'https://official-joke-api.appspot.com/random_joke';

// Make a GET request
fetch(apiUrl)
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
  })