function arrayRangeRec(num = 100, start = 1, arr = []) {
  if (num === 0) return arr;

  arr.push(start);
  return arrayRangeRec(num - 1, start + 1, arr);
}

function arrayRangeLoop(num = 100) {
  arr = [];
  for (let i = 1; i <= num; i++) {
    arr.push(i);
  }
  return arr;
}

function doTimes(times, callback) {
  for (let i = 0; i < times; i++) {
    callback();
  }
}

function timeIt(fn, label = 'It') {
  const start = process.hrtime();
  fn();
  const [elapsedSec, elapsedNanoSec] = process.hrtime(start);
  const ms = Math.round(elapsedSec * 1000 + elapsedNanoSec / 1000000);
  console.log(`${label} took ${ms} ms`);
}

const arrLength = 5000;
const iterations = 1000;

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
