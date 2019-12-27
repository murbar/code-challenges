# def add(a, b):
#     if a < 0 and b < 0:
#         a, b = negate(a), negate(b)
#         return negate(add(a, b))

#     if a < 0:
#         return subtract(b, negate(a))

#     if b < 0:
#         return subtract(a, negate(b))

#     while b != 0:
#         carry = a & b
#         a = a ^ b
#         b = carry << 1

#     return a


# def negate(n):
#     return add(~n, 1)


# def subtract(a, b):
#     negative = True if b > a else False
#     if negative:
#         a, b = b, a

#     while b != 0:
#         borrow = (~a) & b
#         a = a ^ b
#         b = borrow << 1

#     return add(~a, 1) if negative else a


# not my solution
# Python ints are more than 32 bits
# use a mask to get the last 32 bits
def sum(a, b):
    mask = 0xffffffff

    while b & mask:
        carry = a & b
        a = a ^ b
        b = carry << 1

    return (a & mask) if b > mask else a


# assert add(12, 45) == 57
# assert add(-12, -45) == -57
# assert add(12, -45) == -33
# assert add(-12, 45) == 33
# assert add(45, -12) == 33

assert sum(12, 45) == 57
assert sum(-12, -45) == -57
assert sum(12, -45) == -33
assert sum(-12, 45) == 33
assert sum(45, -12) == 33
# assert subtract(45, 12) == 33
# assert subtract(12, 45) == -33
