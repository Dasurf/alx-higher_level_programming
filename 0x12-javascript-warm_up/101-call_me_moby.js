#!/usr/bin/node
exports.callMeMoby = function (n, fn) {
  for (let i = 0; i < n; i++) {
    fn();
  }
};
