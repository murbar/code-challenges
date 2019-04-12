function arrayRangeRec(num = 100, start = 1, arr = []) {
  if (num > 0) {
    arr.push(start);
    // console.log(arr);
    arrayRangeRec(num - 1, start + 1, arr);
  }
  return arr;
}

function arrayRangeLoop(num = 100) {
  arr = [];
  for (let i = 1; i <= num; i++) {
    arr.push(i);
  }
  return arr;
}

function doTimes(times, fn) {
  for (let i = 0; i < times; i++) {
    fn();
  }
}

function timeIt(fn, label = 'It') {
  const start = process.hrtime();
  fn();
  const end = process.hrtime(start);
  console.log(`${label} took ${Math.round(end[0] * 1000 + end[1] / 1000000)}ms`);
}

const arrLength = 99;
const iterations = 1000000;

timeIt(() => {
  doTimes(iterations, () => {
    arrayRangeLoop(arrLength);
  });
}, 'For loop');

timeIt(() => {
  doTimes(iterations, () => {
    arrayRangeRec(arrLength);
  });
}, 'Recursion');

// recursion is about 60% slower
