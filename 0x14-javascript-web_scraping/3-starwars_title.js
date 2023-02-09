#!/usr/bin/node
const request = require('request');
const BASE_URL = 'https://swapi-api.alx-tools.com/api/films/6';

if (process.argv.length > 2) {
  request(`${BASE_URL}/films/${process.argv[2]}/`, (err, res, body) => {
    if (err) {
      console.log(err);
    }
    console.log(JSON.parse(body).title);
  });
}
