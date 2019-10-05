/*
You are at the bottom of a staircase with N stairs. You can jump 1, 2, or 3 stairs at a time. how Many different ways can you jump up the stairs?

N = 3
Answer = 4
1 jump, 1 jump, 1 jump
2 jumps, 1 jump
1 jump, 2 jumps
3 jumps

https://www.youtube.com/watch?v=NFJ3m9a1oJQ

https://github.com/bephrem1/backtobackswe/blob/master/Dynamic%20Programming%2C%20Recursion%2C%20%26%20Backtracking/ClimbingStairs/ClimbingStairs.java
*/

const waysToJump = n => {
  const table = Array(n + 1).fill(0);
  table[0] = 1;
  table[1] = 1;
  table[2] = 2;
  table[3] = 4;

  for (let i = 4; i <= n; i++) {
    table[i] = table[i - 1] + table[i - 2] + table[i - 3];
  }

  return table[n];
};

const waysToJumpConstantSpace = n => {
  const table = [1, 1, 2, 4];

  if (n < table.length) return table[n];

  for (let i = 4; i <= n; i++) {
    table.push(table[1] + table[2] + table[3]);
    table.shift();
  }

  return table[table.length - 1];
};

console.log(waysToJump(54));
console.log(waysToJumpConstantSpace(54));
