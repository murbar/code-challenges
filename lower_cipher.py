chars_in = 'abcdefghijklmnopqrstuvwxyz'
chars_out = chars_in[::-1]


def transform(char):
    if char in chars_in:
        idx = chars_in.index(char)
        return chars_out[idx]
    else:
        return char


def solution(cipher):
    transformed = [transform(c) for c in cipher]
    return ''.join(transformed)


print(solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))
