// https://app.codesignal.com/arcade/intro/level-3/JKKuHJknZNj4YGL32

// Given two strings, find the number of common characters between them.

// For s1 = "aabcc" and s2 = "adcaa", the output should be
// commonCharacterCount(s1, s2) = 3.

// Strings have 3 common characters - 2 "a"s and 1 "c".

function getCounts(str) {
  return str.split('').reduce((obj, char) => {
    if (!obj[char]) obj[char] = 0;
    obj[char]++;
    return obj;
  }, {});
}

function getCommonCount(counts1, counts2) {
  let count = 0;
  for (const c in counts1) {
    if (counts2[c]) {
      count += counts1[c] > counts2[c] ? counts2[c] : counts1[c];
    }
  }
  return count;
}

function commonCharacterCount(s1, s2) {
  return getCommonCount(getCounts(s1), getCounts(s2));
}

const tests = [
  {
    in: ['aabcc', 'adcaa'],
    expectedOut: 3
  },
  {
    in: ['abca', 'xyzbac'],
    expectedOut: 3
  }
];

function runTests(f, tests) {
  tests.forEach((t, i) => {
    const passed = f(...t.in) === t.expectedOut;
    console.log(`Test ${i + 1} ${passed ? 'passed' : 'failed'}`);
  });
}

runTests(commonCharacterCount, tests);
