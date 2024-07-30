#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movieDetails = JSON.parse(body);
    const charactersUrls = movieDetails.characters;

    charactersUrls.forEach(characterUrl => {
      request.get(characterUrl, (err, resp, characterBody) => {
        if (!err && resp.statusCode === 200) {
          const character = JSON.parse(characterBody);
          console.log(character.name);
        }
      });
    });
  } else {
    console.error(error || 'Failed to fetch movie details');
  }
});
