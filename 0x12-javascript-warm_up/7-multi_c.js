#!/usr/bin/node
const x = process.argv[2];
const toNum = Number(x);

if (toNum) {
  for (let i = 0; i < toNum; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
