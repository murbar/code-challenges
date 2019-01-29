// https://www.hackerrank.com/challenges/repeated-string/problem


function repeatedString(s, n) {
    const countA = (arr) => {
        return arr.filter(i => i === 'a').length
    }
    const sArr = [...s];
    const count = countA(sArr);
    const factor = Math.floor(n / s.length);
    const mod = n % s.length;
    const rest = countA(sArr.slice(0, mod))
    return (count * factor) + rest;
}


// tests
const test1s = "aba";
const test1n = 10;
const test1expectedOutput = 7;

const test2s = "babbaabbabaababaaabbbbbbbababbbabbbababaabbbbaaaaabbaababaaabaabbabababaabaabbbababaabbabbbababbaabb";
const test2n = 860622337747;
const test2expectedOutput = 395886275361;

console.log("Test 1 passes:", repeatedString(test1s, test1n) === test1expectedOutput);
console.log("Test 2 passes:", repeatedString(test2s, test2n) === test2expectedOutput);
