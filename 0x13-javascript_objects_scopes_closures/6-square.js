#!/usr/bin/node
module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      this.print(c);
    } else {
      for (let i = 0; i < this.height; i++) console.log(c.repeat(this.width));
    }
  }
};
