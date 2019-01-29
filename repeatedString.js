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


const s = "aba";
const n = 10;
const desired_result = 7;

const s2 = "babbaabbabaababaaabbbbbbbababbbabbbababaabbbbaaaaabbaababaaabaabbabababaabaabbbababaabbabbbababbaabb";
const n2 = 860622337747;
const desired_result2 = 395886275361;

const output = repeatedString(s, n);
console.log(output, "- success:", output === desired_result);

const output2 = repeatedString(s2, n2);
console.log(output2, "- success:", output2 === desired_result2);
