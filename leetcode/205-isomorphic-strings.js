/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Input: s = "egg", t = "add"
Output: true

 */
var isIsomorphic = function (s, t) {
  const mapStoT = new Map();
  const mapTtoS = new Map();
  if (s.length !== t.length) {
    return false;
  }
  for (let i = 0; i < s.length; i++) {
    const charS = s[i];
    const charT = t[i];
    if (!mapStoT.has(charS) && !mapTtoS.has(charT)) {
      mapStoT.set(charS, charT);
      mapTtoS.set(charT, charS);
    }
    if (mapStoT.get(charS) !== charT || mapTtoS.get(charT) !== charS) {
      return false;
    }
  }
  return true;
};

console.log(isIsomorphic('egg', 'add')); // true
console.log(isIsomorphic('foo', 'bar')); // false
console.log(isIsomorphic('f', 'b')); // true
console.log(isIsomorphic('badc', 'baba')); // false
console.log(isIsomorphic('paper', 'title')); // true
