# // https://www.hackerrank.com/challenges/sock-merchant/problem


# n is unused
def sockMerchant(n, ar):
    kinds = set(ar)
    pairs = 0

    for k in kinds:
        pairs += ar.count(k) // 2

    return pairs


test_input = '10 20 20 10 10 30 50 10 20'.split(' ')
expected_output = 3
print("Passes:", sockMerchant(0, test_input) == expected_output)
