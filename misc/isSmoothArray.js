/*
https://app.codesignal.com/challenge/7kZavbM3FBC85FtNA
We define the middle of the array arr as follows:

if arr contains an odd number of elements, its middle is the element whose index number is the same when counting from the beginning of the array and from its end;
if arr contains an even number of elements, its middle is the sum of the two elements whose index numbers when counting from the beginning and from the end of the array differ by one.
An array is called smooth if its first and its last elements are equal to one another and to the middle. Given an array arr, determine if it is smooth or not. */

function getMiddle(arr) {
  const len = arr.length;
  const isEven = len % 2 === 0;
  const i = Math.floor(len / 2);
  return isEven ? arr[i] + arr[i - 1] : arr[i];
}

function isSmooth(arr) {
  return arr[0] === arr[arr.length - 1] && arr[0] === getMiddle(arr);
}

// Tests

const tests = [
  {
    in: [7, 2, 2, 5, 10, 7],
    expectedOut: true
  },
  {
    in: [-5, -5, 10],
    expectedOut: false
  }
];

function runTests(f, tests) {
  tests.forEach((t, i) => {
    const passed = f(t.in) === t.expectedOut;
    console.log(`Test ${i + 1} ${passed ? 'passed' : 'failed'}`);
  });
}

runTests(isSmooth, tests);
