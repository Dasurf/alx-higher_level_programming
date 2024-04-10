#!/usr/bin/node
const fArg = process.argv[2];
const sArg = process.argv[3];

function add (a, b) {
  if (process.argv.length === 4) {
    a = Number(fArg);
    b = Number(sArg);

    if (a && b) {
      console.log(a + b);
    }
  } else {
    console.log(NaN);
  }
}

add(fArg, sArg);
