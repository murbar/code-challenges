// function that takes a roman numeral and returns the integer value

const romanMap = new Map([
  ['I', 1],
  ['V', 5],
  ['X', 10],
  ['L', 50],
  ['C', 100],
  ['D', 500],
  ['M', 1000],
]);

function romanToInt(s: string): number {
  let result = 0;
  let prev = 0;

  for (let i = s.length - 1; i >= 0; i--) {
    const current = romanMap.get(s[i])!;
    if (current < prev) {
      result -= current;
    } else {
      result += current;
    }
    prev = current;
  }

  return result;
}

const testCases = [
  { input: 'III', output: 3 },
  { input: 'IV', output: 4 },
  { input: 'IX', output: 9 },
  { input: 'LVIII', output: 58 },
  { input: 'MCMXCIV', output: 1994 },
];

testCases.forEach(({ input, output }) => {
  const result = romanToInt(input);
  console.log(input, result === output);
});
