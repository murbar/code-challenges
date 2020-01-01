# count vowels in string


import re


def find_vowels(string):
    count = 0
    vowels = 'aeiou'
    for ch in string:
        if ch.lower() in vowels:
            count += 1
    return count


def find_vowels2(string):
    vowels = re.compile(r'[aeiou]')
    return len(vowels.findall(string.lower()))


assert find_vowels('why do you ask?') == 4
assert find_vowels2('why do you ask?') == 4
assert find_vowels2('Oh hi there') == 4
print('All tests passed!')
