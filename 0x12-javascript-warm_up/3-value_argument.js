#!/usr/bin/node
const fs = require('fs');

if (!process.argv[2]) {
    console.log("No argument");
} else {
    console.log(process.argv[2]);
}
