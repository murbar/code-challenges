/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 * We use two pointers, initialized at zero. While each of the pointers are less than the length of the strings, check that the chars at each string's pointer are equal. If so, increment both pointers, else increment only the larger string's pointer. The loop will end when either pointer exceeds the length of the strings. We can then check to see if the subsequence's pointer is at the the last char in the subsequence. If so, the subsequence exists.
 * This could easily be adapted to check values in two arrays.
 * O(n) time, constant space.
 */

var isSubsequence = function (s, t) {
  let sIdx = 0;
  let tIdx = 0;
  while (sIdx < s.length && tIdx < t.length) {
    if (s.charAt(sIdx) === t.charAt(tIdx)) {
      sIdx++;
    }
    tIdx++;
  }
  return sIdx === s.length;
};

// with one pointer and a For loop
var isSubsequenceAlt = function (s, t) {
  let sIdx = 0;
  for (let tIdx = 0; tIdx < t.length; tIdx++) {
    if (sIdx === s.length) {
      break;
    }
    if (s.charAt(sIdx) === t.charAt(tIdx)) {
      sIdx++;
    }
  }
  return sIdx === s.length;
};
