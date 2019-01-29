// https://www.hackerrank.com/challenges/2d-array/problem


function hourglassSum(arr) {
    const sums = [];
    const nRows = arr.length;
    const nCols = arr[0].length;

    for (const row of Array(nRows - 2).keys()) {
        for (const col of Array(nCols - 2).keys()) {
            const [r1, r2, r3] = [arr[row], arr[row+1], arr[row+2]];
            const [c1, c2, c3] = [col, col+1, col+2]
            
            const values = [r1[c1], r1[c2], r1[c3],
                                    r2[c2],
                            r3[c1], r3[c2], r3[c3]];
            
            sums.push(values.reduce((s, v) => s + v));
        }
    }

    return Math.max(...sums);
}

// tests
const input = [[1, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0],
       [0, 0, 2, 4, 4, 0],
       [0, 0, 0, 2, 0, 0],
       [0, 0, 1, 2, 4, 0]]
const expected_output = 19
const output = hourglassSum(input)
console.log(output)
console.log("Passes:", output === expected_output)
