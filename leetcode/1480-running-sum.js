/**
 * @param {number[]} nums
 * @return {number[]}
 */

// In place, modifying the given array as we go.
var runningSum = function (nums) {
  for (let i = 0; i < nums.length; i++) {
    if (i !== 0) {
      nums[i] = nums[i] + nums[i - 1];
    }
  }
  return nums;
};

// Create a new array
var runningSumAlt = function (nums) {
  const running = [];
  for (const n of nums) {
    const i = running.length;
    if (i === 0) {
      running.push(n);
    } else {
      const next = n + running[i - 1];
      running.push(next);
    }
  }
  return running;
};
