#!/usr/bin/node

const args = process.argv;
const id = args[2];

if (id) {
  getFilms(id);
}

async function getFilms (id) {
  const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

  const resp = await fetch(url);

  const movie = await resp.json();

  const characters = movie.characters;

  if (!characters) { return null; }
  for (const i of characters) {
    const re = await fetch(i);
    const character = await re.json();
    const name = character.name;
    console.log(name);
  }
}
