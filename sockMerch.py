
def sockMerchant(n, ar):
    kinds = set(ar)
    pairs = 0
    print(kinds)
    for k in kinds:

        matches = ar.count(k) // 2
        print(k, matches)
        pairs += matches
    return pairs


socks = '1 1 3 1 2 1 3 3 3 3'.split(' ')

print(sockMerchant(5, socks))
