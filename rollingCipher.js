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
