#!/usr/bin/node
/**
 * prints all the characters of a star wars movie
 */

const { argv } = process;
const request = require('request');
const movieURL = 'https://swapi-api.alx-tools.com/api/films';

if (argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js 3');
  process.exit(1);
}

request(`${movieURL}/${argv[2]}`, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const filmData = JSON.parse(body);
  filmData.characters.forEach(character => {
    request(character, (error, res, data) => {
      if (!error) {
        console.log(JSON.parse(data).name);
      }
    });
  });
});
