#!/usr/bin/node
const request = require('request');

if (process.argv.length > 2) {
  request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`, (error, response, body) => {
    if (error) {
      console.log(error);
    }
    const charUrl = JSON.parse(body).characters;
    const charName = charUrl.map(
      url => new Promise((resolve, reject) => {
        request(url, (err, resp, charBody) => {
          if (err) {
            reject(err);
          }
          resolve(JSON.parse(charBody).name);
        });
      }));
    Promise.all(charName)
      .then(names => console.log(names.join('\n')))
      .catch(allError => console.log(allError));
  });
}
