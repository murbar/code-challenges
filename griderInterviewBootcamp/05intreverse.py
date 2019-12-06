

def reverse(n):
    digits = list(str(n))
    digits.reverse()
    if digits[-1] == '-':
        digits.pop()
        digits.insert(0, '-')
    return int(''.join(digits))


assert reverse(51) == 15
assert reverse(-51) == 15
print('All tests passed!')
