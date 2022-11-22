/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 * 
 * We could use two loops but a hashmap is more efficient.
 * Iterate over the array. Keep track of current value and its index.
 * If the complement to the current value is in the map, return the two indexes.
 * Else add the curr and its index to the map, update the index, and go to next value.
 */

var twoSum = function (nums, target) {
  const map = new Map();
  let i = 0;
  for (const n1 of nums) {
    const n2 = target - n1;
    if (map.has(n2)) {
      return [map.get(n2), i];
    }
    map.set(n1, i);
    i++;
  }
};

const nums = [2, 7, 11, 15];
const target = 9;

console.log(twoSum(nums, target));
