const getDigit = (number, place, longestNumber) => {
  const string = number.toString();
  const size = string.length;
  const mod = longestNumber - size;
  return string[place - mod] || 0;
};

const findLongestNumber = array => {
  return array.reduce((longest, number) => {
    const length = number.toString().length;
    return length > longest ? length : longest;
  }, 0);
};

const radixSort = array => {
  const longestNumber = findLongestNumber(array);
  const buckets = Array.from({ length: 10 }, () => []);
  for (let i = longestNumber - 1; i >= 0; i--) {
    while (array.length) {
      const current = array.shift();
      buckets[getDigit(current, i, longestNumber)].push(current);
    }

    for (let j = 0; j < 10; j++) {
      while (buckets[j].length) {
        array.push(buckets[j].shift());
      }
    }
  }
  return array;
};

const unsorted = [
  20,
  51,
  3,
  801,
  415,
  62,
  4,
  17,
  19,
  11,
  1,
  100,
  1244,
  104,
  944,
  854,
  34,
  3000,
  3001,
  1200,
  633
];
const sorted = [
  1,
  3,
  4,
  11,
  17,
  19,
  20,
  34,
  51,
  62,
  100,
  104,
  415,
  633,
  801,
  854,
  944,
  1200,
  1244,
  3000,
  3001
];

console.assert(JSON.stringify(radixSort(unsorted)) === JSON.stringify(sorted));
