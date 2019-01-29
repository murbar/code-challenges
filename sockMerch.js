// https://www.hackerrank.com/challenges/sock-merchant/problem


function sockMerchant(n, ar) {
    const kinds = [...new Set(ar)];
    return kinds.reduce((pairs, k) => {
        return pairs += Math.floor(ar.filter(j => j === k).length / 2)
    }, 0);
}

const arr = [10, 20, 20, 10, 10, 30, 50, 10, 20];
const desiredOutput = 3;

const result = sockMerchant(1, arr); // only use second param
console.log(result);
console.assert(result === desiredOutput);