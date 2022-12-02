const sum = function (nums: string[] | number[]) {
  return nums.reduce((tot, cur) => tot + parseInt(cur), 0);
};

const text = await Deno.readTextFile('input.txt');
const totals = text.split('\n\n').map((txt) => sum(txt.split('\n')));
totals.sort((a, b) => b - a);
const solutionA = totals[0];
const solutionB = sum(totals.slice(0, 3));
console.log({ solutionA, solutionB });
