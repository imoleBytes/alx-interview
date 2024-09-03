#!/usr/bin/node
const request = require('request');

const args = process.argv;
const id = args[2];

if (id) {
  getFilmCharacters(id);
}

// async function getFilms (id) {
//   const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

//   const resp = await fetch(url);

//   const movie = await resp.json();

//   const characters = movie.characters;

//   if (!characters) { return null; }
//   for (const i of characters) {
//     const re = await fetch(i);
//     const character = await re.json();
//     const name = character.name;
//     console.log(name);
//   }
// }

function getFilmCharacters (movieID) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

  request(url, (err, response, body) => {
    if (err) {
      return;
    }
    if (response.statusCode === 200) {
      const characters = JSON.parse(body).characters;
      printCharacterName(characters, 0);
    }
  });
}

// function printName (characters) {
//   if (!characters) { return null; }
//   for (let i = 0; i < characters.length; i++) {
//     const re = request(characters[i], (err, response, body) => {
//         let name = JSON.parse(body)["name"];
//         console.log(name);
//     });
//   }
// }

function printCharacterName (characters, idx) {
  if (idx === characters.length) { return; }
  request(characters[idx], (err, response, body) => {
    console.log(JSON.parse(body).name);
    printCharacterName(characters, idx + 1);
  });
}
