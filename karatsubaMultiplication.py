# recursively computer the product of two integers
# https://www.codeandgadgets.com/karatsuba-multiplication-python/


def zeroPad(numberString, zeros, left=True):
    """Return the string with zeros added to the left or right."""
    for i in range(zeros):
        if left:
            numberString = '0' + numberString
        else:
            numberString = numberString + '0'
    return numberString


def multiplyByAddition(x, y):
    """Multiply two integers using repeated addition."""
    product = 0
    for _ in range(y):
        product = product + x
    return product


def karatsubaMultiplication(x, y):
    """Multiply two integers using Karatsuba's algorithm."""
    # convert to strings for easy access to digits
    x = str(x)
    y = str(y)
    # base case for recursion
    if len(x) == 1 and len(y) == 1:
        return multiplyByAddition(int(x), int(y))
    if len(x) < len(y):
        x = zeroPad(x, len(y) - len(x))
    elif len(y) < len(x):
        y = zeroPad(y, len(x) - len(y))
    n = len(x)
    j = n//2
    # for odd digit integers
    if (n % 2) != 0:
        j += 1
    BZeroPadding = n - j
    AZeroPadding = BZeroPadding * 2
    a = int(x[:j])
    b = int(x[j:])
    c = int(y[:j])
    d = int(y[j:])
    # recursively calculate
    ac = karatsubaMultiplication(a, c)
    bd = karatsubaMultiplication(b, d)
    k = karatsubaMultiplication(a + b, c + d)
    A = int(zeroPad(str(ac), AZeroPadding, False))
    B = int(zeroPad(str(k - ac - bd), BZeroPadding, False))
    return A + B + bd


assert karatsubaMultiplication(5678, 1234) == 5678 * 1234
assert karatsubaMultiplication(56789, 1234) == 56789 * 1234
assert karatsubaMultiplication(5678, 123) == 5678 * 123

assert karatsubaMultiplication(
    3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627) == 3141592653589793238462643383279502884197169399375105820974944592 * 2718281828459045235360287471352662497757247093699959574966967627
