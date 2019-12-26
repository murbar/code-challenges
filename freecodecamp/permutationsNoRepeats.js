// https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/no-repeats-please

// https://www.youtube.com/watch?v=IPWmrjE1_MU
// https://en.wikipedia.org/wiki/Heap%27s_algorithm

// permute an array

function swap(arr, i, j) {
  const temp = arr[i];
  arr[i] = arr[j];
  arr[j] = temp;
}

function permuteArray(array, startIndex, results) {
  if (startIndex >= array.length) {
    results.push([...array]);
  } else {
    for (let i = startIndex; i < array.length; i++) {
      swap(array, startIndex, i);
      permuteArray(array, startIndex + 1, results);
      swap(array, startIndex, i);
    }
  }
}

// a bit more straightforward for strings

function permuteString(prefix, suffix, results) {
  if (suffix.length === 0) {
    results.push(prefix);
  } else {
    for (let i = 0; i < suffix.length; i++) {
      permuteString(
        prefix + suffix[i],
        suffix.slice(0, i) + suffix.slice(i + 1),
        results
      );
    }
  }
}

function permutations(string) {
  results = [];
  permuteString('', string, results);
  return results;
}

function permutationsArray(arr) {
  results = [];
  permuteArray(arr, 0, results);
  return results;
}

console.log(permutations('abc'));
console.log(permutationsArray([1, 2, 3]));

// problem function
function permAlone(str) {
  const repeats = /([a-z])\1/;
  const noRepeats = permutations(str).filter(s => !repeats.test(s));
  return noRepeats.length;
}

permAlone('aabb');
