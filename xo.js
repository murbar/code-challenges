// Return true if the string contains the same number of Xs as Os

function XO(str) {
  const arr = [...str];
  const xs = arr.filter(c => c === 'x').length;
  const os = arr.filter(c => c === 'o').length;
  return xs === os;
}

console.log(XO('xoxooxox'));
