
def reverse(string):
    l = list(string)
    l.reverse()
    return ''.join(l)


def reverse2(string):
    reversed = []
    for ch in string:
        reversed.insert(0, ch)
    return ''.join(reversed)


def reverse3(string):
    reversed = ''
    for ch in string:
        reversed = ch + reversed
    # could be done with reduce in JS
    return reversed


assert reverse('joel') == 'leoj'
assert reverse2('joel') == 'leoj'
assert reverse3('joel') == 'leoj'
