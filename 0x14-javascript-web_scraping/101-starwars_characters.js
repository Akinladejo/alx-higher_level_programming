#!/usr/bin/node

const request = require('request');

function printCharacters (characters, index) {
  if (index < characters.length) {
    request(characters[index], function (error, response, body) {
      if (!error && response.statusCode === 200) {
        const character = JSON.parse(body).name;
        console.log(character);
        printCharacters(characters, index + 1);
      }
    });
  }
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movieDetails = JSON.parse(body);
    const charactersUrls = movieDetails.characters;
    printCharacters(charactersUrls, 0);
  } else {
    console.error(error || 'Failed to fetch movie details');
  }
});
