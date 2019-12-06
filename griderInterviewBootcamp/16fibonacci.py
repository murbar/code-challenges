# good for comparing runtime complexity of different solutions
# return Nth fibonacci element
# good candidate for memoization


def fib(n):
    # linear time and space
    series = [0, 1]

    for i in range(2, n+1):
        a, b = series[i-1], series[i-2]
        series.append(a + b)

    return series[-1]


def fibR(n):
    # exponential runtime
    if n < 2:
        return n

    return fibR(n-1) + fibR(n-2)

# we can memoize this with a generic memoize function
# would be a good usecase for a decorator so we don't hav eto overwrite the function name


def memoize(fn):
    cache = {}

    def helper(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]

    return helper


def fibRM(n, memo={}):
    # memo refers to the same dictionary on every call
    if n < 2:
        return n

    if n not in memo:
        memo[n] = fibRM(n-1) + fibRM(n-2)
    return memo[n]


assert fib(4) == 3
assert fib(10) == 55
assert fib(50) == 12586269025
assert fibR(4) == 3
assert fibR(10) == 55
assert fibRM(4) == 3
assert fibRM(10) == 55
assert fibRM(50) == 12586269025
print('All tests passed!')
