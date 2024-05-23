#!/usr/bin/node
/**
 * prints all the characters of a star wars movie
 */

const { argv } = process;
const request = require('request');

if (argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js 3');
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}`;
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return
  }
  const filmData = JSON.parse(body);
  if (!filmData) {
    console.error('Invalid movie id')
  }
  filmData.characters.forEach(characterUrl => {
    request(characterUrl, (characterError, characterResponse, characterBody) => {
      if (characterError) {
        console.error(characterError)
        return
      }
      const characterData = JSON.parse(characterBody);
      console.log(characterData.name);
    });
  });
});
