/*
https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/smallest-common-multiple

Find the smallest common multiple of the provided parameters that can be evenly divided by both, as well as by all sequential numbers in the range between these parameters.

The range will be an array of two numbers that will not necessarily be in numerical order.

For example, if given 1 and 3, find the smallest common multiple of both 1 and 3 that is also evenly divisible by all numbers between 1 and 3. The answer here would be 6.
*/

function smallestCommon(arr) {
  let [a, b] = arr;
  if (a > b) {
    [a, b] = [b, a];
  }
  let scm = a * b;
  while (true) {
    let found = true;

    for (let i = a; i <= b; i++) {
      const valid = [a, b, i].every(n => scm % n === 0);
      if (!valid) {
        found = false;
        break;
      }
    }

    if (found) {
      return scm;
    } else {
      scm++;
    }
  }
}
