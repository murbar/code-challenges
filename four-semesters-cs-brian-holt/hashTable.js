class HashTableSet {
  size = 255;

  constructor() {
    this.table = new Array(this.size);
  }

  hash(input, max) {
    let num = 0;
    for (let i = 0; i < input.length; i++) {
      num += input.charCodeAt(i) * i;
    }
    return num % max;
  }

  getIndex(input) {
    return this.hash(input, this.size);
  }

  add(input) {
    this.table[this.getIndex(input)] = input;
  }

  check(input) {
    return !!this.table[this.getIndex(input)];
  }
}

('use strict');

function hash(str) {
  var hash = 5381,
    i = str.length;

  while (i) {
    hash = (hash * 33) ^ str.charCodeAt(--i);
  }

  return hash >>> 0;
}

module.exports = hash;
