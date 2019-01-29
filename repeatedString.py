# https://www.hackerrank.com/challenges/repeated-string/problem


def repeatedString(s, n):
    if len(s) == 1:
        return n

    # naive solution, very inefficient on large inputs
    # factor = n // len(s)
    # test_str = s * (factor + 1)
    # test_str = test_str[:n]
    # return list(test_str).count('a')

    count = list(s).count('a')
    factor = n // len(s)
    mod = n % len(s)
    rest = s[:mod].count('a')
    return (count * factor) + rest


# tests
test1_s = "aba"
test1_n = 10
test1_expected = 7

test2_s = "babbaabbabaababaaabbbbbbbababbbabbbababaabbbbaaaaabbaababaaabaabbabababaabaabbbababaabbabbbababbaabb"
test2_n = 860622337747
test2_expected = 395886275361

print("Test 1 passes:", repeatedString(test1_s, test1_n) == test1_expected)
print("Test 2 passes:", repeatedString(test2_s, test2_n) == test2_expected)
