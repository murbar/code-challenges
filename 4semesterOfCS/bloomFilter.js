function simpleHash(str, seed, mod) {
  let hash = seed;
  let i = str.length;
  while (i) hash = (hash * 33) ^ str.charCodeAt(--i);
  return (hash >>> 0) % mod;
}

class BloomFilter {
  constructor(size = 500) {
    this.hashSeeds = [5381, 1835, 7811];
    this.size = size;
    this.vector = Array(size).fill(0);
  }

  getIndexes(string) {
    return this.hashSeeds.map(s => simpleHash(string, s, this.size));
  }

  add(string) {
    const indexes = this.getIndexes(string);
    console.log(indexes);
    indexes.forEach(i => (this.vector[i] = 1));
  }

  contains(string) {
    const indexes = this.getIndexes(string);
    return indexes.every(i => !!this.vector[i]);
  }
}

const bf = new BloomFilter();
bf.add('joel');
bf.add('jack');
bf.add('jill');
console.log(bf.contains('joel'));
console.log(bf.contains('lola'));
