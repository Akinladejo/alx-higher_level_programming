#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
	if (!error && response.statusCode === 200) {
		fs.writeFile(filePath, body, 'utf-8', (err) => {
			if (err) {
				console.error(err);
				}
			});
		}
	else {
		console.error(error || 'Failed to fetch data');
		}
	});
