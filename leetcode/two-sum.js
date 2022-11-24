/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 *
 * We could use two loops but a hashmap is more efficient.
 * Iterate over the array. Keep track of current value and its index.
 * If the complement to the current value is in the map, return the two indexes.
 * Else add the curr and its index to the map, update the index, and go to next value.
 * O(N) time & space
 *
 * Alternatively: we could sort the array and use two pointers, one at each end. Sum numbers at the pointers. Is the sum equal to the target? If sum is less than target, move right pointer to left, if target is greater, move left pointer to the right. Check and repeat.
 * This will gives up the two numbers. But less useful if we need to return the indexes.
 * Good sort algos are O(log N) time.
 * O(log N) time, constant space.
 */

var twoSum = function (numsArray, target) {
  const map = new Map();
  let i = 0;
  for (const n1 of numsArray) {
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
