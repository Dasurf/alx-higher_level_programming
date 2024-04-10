#!/usr/bin/node
exports.addMeMaybe = function (n, incrFn) {
  n++;
  incrFn(n);
};
