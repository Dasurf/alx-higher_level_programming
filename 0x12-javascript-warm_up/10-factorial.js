#!/usr/bin/node
const arg = process.argv[2];

function factorial (num) {
  let Integer = Number(num);
  if (Integer === 0 || Integer === 1 || isNaN(Integer)) {
    return 1;
  }
  Integer *= factorial(num - 1);
  return Integer;
}

const sample = factorial(arg);
console.log(sample);
