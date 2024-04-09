#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (w, h) {
    w = this.width;
    h = this.height;
    let str = '';

    for (let j = 1; j <= h; j++) {
      for (let i = 1; i <= w; i++) {
        str += 'X';
      }
      if (j !== h) {
        str += '\n';
      }
    }
    return str;
  }
}

module.exports = Rectangle;
//   export default Rectangle;
