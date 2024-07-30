#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const todos = JSON.parse(body);
    const completedTasks = {};

    todos.forEach(todo => {
      if (todo.completed) {
        completedTasks[todo.userId] = (completedTasks[todo.userId] || 0) + 1;
      }
    });

    console.log(completedTasks);
  } else {
    console.error(error || 'Failed to fetch data');
  }
});
