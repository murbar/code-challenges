// O(2^N) time, O(N) space - BAD!
function fibRecursiveNaive(n: number): number {
  if (n <= 1) {
    return n;
  }
  return fibRecursiveNaive(n - 1) + fibRecursiveNaive(n - 2);
}

// O(N) time, O(N) space
function fibRecursiveMemoized(n: number, memo = new Map()): number {
  if (memo.has(n)) {
    return memo.get(n);
  }
  if (n <= 1) {
    return n;
  }
  const result = fibRecursiveMemoized(n - 1, memo) + fibRecursiveMemoized(n - 2, memo);
  memo.set(n, result);
  return result;
}

// O(N) time, O(1) space
function fibIterative(n: number): number {
  if (n <= 1) {
    return n;
  }
  let prev = 0;
  let curr = 1;
  for (let i = 2; i <= n; i++) {
    const temp = curr;
    curr += prev;
    prev = temp;
  }
  return curr;
}

const testCases = [
  [0, 0],
  [1, 1],
  [9, 34],
  [24, 46368],
];

testCases.forEach(([input, expected]) => {
  const actual = fibIterative(input);
  console.assert(
    actual === expected,
    `fibRecursive(${input}) === ${expected}, but got ${actual}`
  );
});
