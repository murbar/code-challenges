// https://www.hackerrank.com/challenges/sock-merchant/problem


// n is unused in this solution
function sockMerchant(n, ar) {
    const kinds = [...new Set(ar)];
    return kinds.reduce((pairs, k) => {
        return pairs += Math.floor(ar.filter(j => j === k).length / 2)
    }, 0);
}


// tests
const input = [10, 20, 20, 10, 10, 30, 50, 10, 20];
const expectedOutput = 3;
console.log('Test 1 passes:', sockMerchant(0, input) === expectedOutput);
