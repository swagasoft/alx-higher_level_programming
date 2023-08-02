#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const args = process.argv;
const url = args[2];
const filePath = args[3];

request(
  {
    method: 'GET',
    uri: url
  },
  function (error, response, body) {
    if (error) throw error;
    if (response.statusCode === 200) {
      fs.writeFile(filePath, body, 'utf8', function (error) {
        if (error) throw error;
      });
    }
  }
);
