// https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

function rotLeft(a, d) {
  return [...a.slice(d), ...a.slice(0, d)];
}

// tests
const test_a = [1, 2, 3, 4, 5];
const test_d = 4;
const expected_output = [5, 1, 2, 3, 4];
console.log(
  'Passes:',
  rotLeft(test_a, test_d).toString() === expected_output.toString()
);
