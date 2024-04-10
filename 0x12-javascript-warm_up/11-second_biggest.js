#!/usr/bin/node
const args = process.argv;
const [, , ...rest] = args;

if (rest.length === 0 || rest.length === 1) {
  console.log(0);
} else {
  const sortedArr = rest.sort((a, b) => Number(b) - Number(a));
  console.log(sortedArr[1]);
}
