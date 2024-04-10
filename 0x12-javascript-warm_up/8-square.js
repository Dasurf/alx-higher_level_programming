#!/usr/bin/node
const size = process.argv[2];
const sizeToNum = Number(size);

if (sizeToNum) {
  let str = '';
  for (let i = 0; i < sizeToNum; i++) {
    str += 'X';
  }
  for (let i = 0; i < sizeToNum; i++) {
    console.log(str);
  }
} else {
  console.log('Missing size');
}
