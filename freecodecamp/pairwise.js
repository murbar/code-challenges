//www.freecodecamp.org/learn/coding-interview-prep/algorithms/pairwise

function pairwise(arr, arg) {
  if (arr.length === 0) {
    return 0;
  }

  let indexes = [];
  const compliments = {};

  for (let i = 0; i < arr.length; i++) {
    const curr = arr[i];
    const comp = arg - curr;

    if (compliments.hasOwnProperty(comp)) {
      const j = compliments[comp].shift();
      if (j !== undefined) {
        indexes = [...indexes, i, j];
      }
    } else {
      if (compliments.hasOwnProperty(curr)) {
        compliments[curr].push(i);
      } else {
        compliments[curr] = [i];
      }
    }
  }

  return indexes.reduce((a, b) => a + b);
}

console.assert(pairwise([1, 4, 2, 3, 0, 5], 7) === 11);
console.assert(pairwise([1, 3, 2, 4], 4) === 1);
console.assert(pairwise([1, 1, 1], 2) === 1);
console.assert(pairwise([0, 0, 0, 0, 1, 1], 1) === 10);
console.assert(pairwise([], 100) === 0);
