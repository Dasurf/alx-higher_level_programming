#!/usr/bin/node
const dict = require('./101-data').dict;

const totalLlist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDict = {};
for (const j in valsUniq) {
  const list = [];
  for (const k in totalLlist) {
    if (totalLlist[k][1] === valsUniq[j]) {
      list.push(totalLlist[k][0]);
    }
  }
  newDict[valsUniq[j]] = list;
}
console.log(newDict);
