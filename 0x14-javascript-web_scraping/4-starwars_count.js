#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
let count = 0;

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const films = JSON.parse(body).results;
    for (const film of films) {
      for (const characterUrl of film.characters) {
        if (characterUrl.endsWith('/18/')) {
          count++;
          break;
        }
      }
    }
    console.log(count);
  } else {
    console.log(error || 'Failed to fetch data');
  }
});
