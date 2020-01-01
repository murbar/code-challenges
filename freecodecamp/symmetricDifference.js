// https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/find-the-symmetric-difference

function sym(...arrays) {
  const counts = {};
  const result = [];
  arrays.forEach(arr => {
    [...new Set(arr)].forEach(n => {
      if (counts[n]) {
        counts[n]++;
      } else {
        counts[n] = 1;
      }
    });
  });

  for (const c in counts) {
    if (counts[c] % 2 === 1) {
      result.push(Number(c));
    }
  }

  return result;
}

sym([1, 2, 5], [2, 3, 5], [3, 4, 5]);
