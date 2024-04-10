#!/usr/bin/node

// creating a function that is visible from other files
exports.add = function add(a, b) {
  return a + b;
}

const add = require('13-add.js');
console.log(add(3, 7));
