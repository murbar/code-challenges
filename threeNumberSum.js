/*
Three Number Sum
Write a function that takes in a non-empty array of distinct integers and a target integer. Your function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets. Each inner array containing a single triplet should have all three of its elements ordered in ascending order. The triplets themselves should be ordered in ascending order with respect to the first number of each triplet. 

If no such triplets can be found in the array, your function should return an empty array. 

Example 1:
Input: [12, 3, 1, 2, -6, 5, -8, 6], 0
Expected Output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

Example 2: 
Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 30

Expected Output: [[6, 9, 15], [7, 8, 15]]
*/

function grossArraySort(a, b) {
  if (a[0] - b[0] === 0) {
    if (a[1] - b[1] === 0) {
      return a[2] - b[2];
    } else {
      return a[1] - b[1];
    }
  } else {
    return a[0] - b[0];
  }
}

function threeNumberSum(arr, target) {
  const triplets = [];

  for (let i of arr) {
    for (let j of arr) {
      for (let k of arr) {
        if (i === j || i === k || j === k) continue;
        if (i + j + k === target) {
          const resultRepr = [i, j, k].sort().join(',');
          if (!triplets.includes(resultRepr)) {
            triplets.push(resultRepr);
          }
        }
      }
    }
  }

  return triplets.map(repr => repr.split(',')).sort(grossArraySort);
}

// https://medium.com/@paulrohan/solving-the-classic-two-sum-and-three-sum-problem-in-javascript-7d5d1d47db03
function threeNumberSumImproved(arr, target) {
  arr.sort((a, b) => a - b);

  const triplets = [];

  for (let iA = 0; iA < arr.length - 2; iA++) {
    const a = arr[iA];

    if (a > target) return triplets;
    if (a === arr[iA - 1]) continue;

    let iB = iA + 1;
    let iC = arr.length - 1;

    while (iB < iC) {
      const b = arr[iB];
      const c = arr[iC];

      if (a + b + c === target) {
        triplets.push([a, b, c]);
      }

      if (a + b + c >= target) {
        while (arr[iC - 1] === c) {
          iC--;
        }
        iC--;
      }

      if (a + b + c <= target) {
        while (arr[iB + 1] === b) {
          iB++;
        }
        iB++;
      }
    }
  }

  return triplets.sort(grossArraySort);
}

console.log(threeNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 30));
console.log(threeNumberSumImproved([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 30));
