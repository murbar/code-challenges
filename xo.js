function XO(str) {
  const arr = [...str];
  const xs = arr.filter(c => c === 'x').length;
  const os = arr.filter(c => c === 'o').length;
  return xs === os;
}

console.log(XO('xoxooxox'));
