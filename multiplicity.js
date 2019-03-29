// Write a function that accepts an array of numbers and returns an array of elements [number, multiplicity] for each number passed into it. The multiplicity of a number refers to the number of times it occurs in the array.

// Ex:
// [5, 5, 1, 1, 5, 5, 3]
// [[5, 4], [1, 2], [3, 1]]
// // Since 5 appears 4 times, 1 appears twice, and 3 appears once.
// The final array should only include unique elements, and the elements should be ordered by when they first appeared in the original array.

function multiplicity(numbers) {
  return numbers.reduce((counts, n) => {
    const index = counts.findIndex(c => c[0] === n);
    if (index !== -1) {
      counts[index][1] += 1;
      return counts;
    } else {
      counts.push([n, 1]);
      return counts;
    }
  }, []);
}

// Examples:
console.log(multiplicity([1, 1, 1, 2, 2, 3])); // [[1, 3], [2, 2], [3, 1]]

console.log(multiplicity([5, 5, 1, 1, 5, 5, 3])); // [[5, 4], [1, 2], [3, 1]]

console.log(multiplicity([1, 1, 1, 1, 1])); // [[1, 5]]

console.log(multiplicity([1, 5, 4, 3, 2])); // [[1, 1], [5, 1], [4, 1], [3, 1], [2, 1]]
