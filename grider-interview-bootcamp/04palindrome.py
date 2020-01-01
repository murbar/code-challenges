
def palindrome(string):
    l = list(string)
    l.reverse()
    return string == ''.join(l)


def palindrome2(string):
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - (i+1)]:
            return False
    return True


assert palindrome('abba') == True
assert palindrome('joel') == False
assert palindrome2('abbba') == True
assert palindrome2('joel') == False
print('All test passed!')
