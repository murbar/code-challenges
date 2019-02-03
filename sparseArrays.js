// https://www.hackerrank.com/challenges/sparse-arrays/problem

function matchingStrings(strings, queries) {
  const results = new Array(queries.length).fill(0);

  for (const s of strings)
    for (const [i, q] of queries.entries()) if (s === q) results[i]++;

  return results;
}

// tests
const testStrings = [
  'abcde',
  'sdaklfj',
  'asdjf',
  'na',
  'basdn',
  'sdaklfj',
  'asdjf',
  'na',
  'asdjf',
  'na',
  'basdn',
  'sdaklfj',
  'asdjf'
];
const testQueries = ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn'];
const expectedOutput = [1, 3, 4, 3, 2];
console.log(
  'Passes:',
  matchingStrings(testStrings, testQueries).toString() ===
    expectedOutput.toString()
);
