const numeralMap = {
  M: 1000,
  CM: 900,
  D: 500,
  CD: 400,
  C: 100,
  XC: 90,
  L: 50,
  XL: 40,
  X: 10,
  IX: 9,
  V: 5,
  IV: 4,
  I: 1
};

function convertToRoman(int) {
  let roman = '';

  for (let [num, val] of Object.entries(numeralMap)) {
    while (int >= val) {
      roman += num;
      int -= val;
    }
  }

  return roman;
}
