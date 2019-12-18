const getCharCode = ch => ch.charCodeAt(0);

const isUpperAlpha = ch => {
  const c = getCharCode(ch);
  return c >= getCharCode('A') && c <= getCharCode('Z');
};

const translateCharCode = (ch, delta) => {
  const offsetA = getCharCode('A');
  return ((getCharCode(ch) - offsetA + delta) % 26) + offsetA;
};

function rot13(str) {
  let result = '';

  for (let ch of str) {
    if (isUpperAlpha(ch)) {
      const newCode = translateCharCode(ch, 13);
      result += String.fromCharCode(newCode);
    } else {
      result += ch;
    }
  }

  return result;
}
