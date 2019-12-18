// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/javascript-algorithms-and-data-structures-projects/telephone-number-validator

function telephoneCheck(str) {
  const re = /^1?\s?(\(\d{3}\)|\d{3})[\s-]?\d{3}[\s-]?\d{4}$/;
  return re.test(str);
}

console.assert(telephoneCheck('1 555-555-5555'));
console.assert(telephoneCheck('1 555-555-5555'));
console.assert(telephoneCheck('1 (555) 555-5555'));
console.assert(telephoneCheck('5555555555'));
console.assert(telephoneCheck('555-555-5555'));
console.assert(telephoneCheck('(555)555-5555'));
console.assert(telephoneCheck('1(555)555-5555'));
console.assert(!telephoneCheck('555-5555'));
console.assert(!telephoneCheck('5555555'));
console.assert(!telephoneCheck('1 555)555-5555'));
console.assert(telephoneCheck('1 555 555 5555'));
console.assert(telephoneCheck('1 456 789 4444'));
console.assert(!telephoneCheck('123**&!!asdf#'));
console.assert(!telephoneCheck('55555555'));
console.assert(!telephoneCheck('(6054756961)'));
console.assert(!telephoneCheck('2 (757) 622-7382'));
console.assert(!telephoneCheck('0 (757) 622-7382'));
console.assert(!telephoneCheck('-1 (757) 622-7382'));
console.assert(!telephoneCheck('2 757 622-7382'));
console.assert(!telephoneCheck('10 (757) 622-7382'));
console.assert(!telephoneCheck('27576227382'));
console.assert(!telephoneCheck('(275)76227382'));
console.assert(!telephoneCheck('2(757)6227382'));
console.assert(!telephoneCheck('2(757)622-7382'));
console.assert(!telephoneCheck('555)-555-5555'));
console.assert(!telephoneCheck('(555-555-5555'));
console.assert(!telephoneCheck('(555)5(55?)-5555'));
