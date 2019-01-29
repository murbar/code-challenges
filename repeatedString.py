# https://www.hackerrank.com/challenges/repeated-string/problem


def repeatedString(s, n):
    if len(s) == 1:
        return n

    # very inefficient on large inputs
    # factor = n // len(s)
    # test_str = s * (factor + 1)
    # test_str = test_str[:n]
    # return list(test_str).count('a')

    count = list(s).count('a')
    factor = n // len(s)
    mod = n % len(s)
    rest = s[:mod].count('a')
    return (count * factor) + rest
    # or the ugly way
    # return (list(s).count('a') * (n // len(s))) + s[:(n % len(s))].count('a')


s = "aba"
n = 10
desired_result = 7

s2 = "babbaabbabaababaaabbbbbbbababbbabbbababaabbbbaaaaabbaababaaabaabbabababaabaabbbababaabbabbbababbaabb"
n2 = 860622337747
desired_result2 = 395886275361

output = repeatedString(s, n)
print(output, "- success:", output == desired_result)

output2 = repeatedString(s2, n2)
print(output2, "- success:", output2 == desired_result2)
