//  https://www.hackerrank.com/challenges/diagonal-difference/problem

function diagonalDifference(arr) {
    let l2r = 0;
    let r2l = 0;

    for (let [i, row] of arr.entries()) {
        l2r += row[i];
        const reversed = [...row].reverse();
        r2l += reversed[i];
    }

    return Math.abs(l2r - r2l);
}

const input = [[11, 2, 4], [4, 5, 6], [10, 8, -12]];
const output = 15;

console.log(diagonalDifference(input)); // -> 15
console.assert(diagonalDifference(input) === 15);