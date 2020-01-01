// https://app.codesignal.com/arcade/intro/level-3/fzsCQGYbxaEcTr2bL

// Given an array of strings, return another array containing all of its longest strings.

// For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
// allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

function allLongestStrings(inputArray) {
  const longestLen = inputArray.reduce((longest, current) => {
    return current.length > longest ? current.length : longest;
  }, 0);
  return inputArray.filter(i => i.length === longestLen);
}

inputArray = ['aba', 'aa', 'ad', 'vcd', 'aba'];
expectedOutput = ['aba', 'vcd', 'aba'];
console.log(
  'Test passed: ',
  JSON.stringify(allLongestStrings(inputArray)) == JSON.stringify(expectedOutput)
);
