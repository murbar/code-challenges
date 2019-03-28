function rollingCipher(string, num) {
  const alpha = 'abcdefghijklmnopqrstuvwxyz';
  const chars = string.split('');
  return chars
    .map(c => {
      let newIndex = alpha.indexOf(c) + num;
      if (newIndex < 0) {
        newIndex = 26 + newIndex;
      } else {
        newIndex = newIndex % 26;
      }
      return alpha[newIndex];
    })
    .join('');
}

console.log(rollingCipher('abcd', 55));

//Make a cipher: write a function that accepts a string and a number (n) and returns a cipher by rolling each character forward (n > 0) or backward (n < 0) n times.

//Examples:
rollingCipher('abcd', 1); //"bcde"

rollingCipher('abcd', -1); //"zabc"

rollingCipher('abcd', 3); //"defg"

rollingCipher('abcd', 26); //"abcd"

// Notes:
// -All letters are lower cased.
// -Expect no spacing.
// -Each character is rotated the same number of times.
// -Think of the letters as a connected loop, so rolling a backwards once will yield z, and rolling z forward once will yield a. If you roll 26 times in either direction, you should end up back where you started.
