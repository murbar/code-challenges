# https://leetcode.com/problems/count-and-say/


def count_vals(say_str):
    result = ''
    val = say_str[0]
    freq = 1
    for i in range(1, len(say_str)):
        curr = say_str[i]
        if curr == val:
            freq += 1
        else:
            result += f'{freq}{val}'
            val = curr
            freq = 1

    result += f'{freq}{val}'
    return result


def countAndSay(n: int) -> str:
    cur = '1'
    nxt = count_vals(cur)
    while n > 1:
        cur = nxt
        nxt = count_vals(cur)
        n -= 1

    return cur


assert countAndSay(1) == '1'
assert countAndSay(2) == '11'
assert countAndSay(3) == '21'
assert countAndSay(4) == '1211'
assert countAndSay(5) == '111221'
assert countAndSay(12) == '3113112221232112111312211312113211'
