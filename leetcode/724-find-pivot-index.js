/**
 * @param {number[]} nums
 * @return {number}
 *
 * Given an array of integers nums, calculate the pivot index of this array.
 *
 * The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
 *
 * If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
 *
 * Return the leftmost pivot index. If no such index exists, return -1.
 */
var pivotIndex = function (nums) {
  let sum = nums.reduce((total, curr) => total + curr, 0);
  let leftSum = 0;
  for (let i = 0; i < nums.length; i++) {
    const curr = nums[i];
    if (leftSum === sum - leftSum - curr) {
      return i;
    }
    leftSum = leftSum + curr;
  }
  return -1;
};
