def conditinals(n):
    w = 'Weird'
    nw = 'Not Weird'
    is_even = n % 2 == 0
    if not is_even:
        print('1')
        return w
    if (2 <= n and n <= 5):
        print('2')
        return nw
    if (6 <= n and n <= 20):
        print('3')
        return w
    if n > 20:
        print('4')
        return nw


print(conditinals(18))
