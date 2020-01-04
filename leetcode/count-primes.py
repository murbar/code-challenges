# https://leetcode.com/problems/count-primes/

# count all prime numbers less than n
# need a function to determine if a number is prime


class Solution:
    def countPrimes(self, n: int) -> int:
        # too slow for large inputs

        def is_prime(num):
            i = 2
            while i * i <= num:
                if num % i == 0:
                    return False
                i += 1

            return num >= 2

        count = 0
        for i in range(2, n):
            if is_prime(i):
                count += 1

        return count

    def countPrimes2(self, n: int) -> int:
        # using sieve of Eratosthenes
        # faster, but requires memory to store potentially large list of values
        # vector ~1MB * n/125,000, eg. 16MB with n of 2,000,000
        # would use a true bit vector to minimize memory footprint
        vector = [True] * (n+1)
        p = 2
        while p * p <= n:
            if vector[p]:
                for i in range(p * p, n + 1, p):
                    vector[i] = False
            p += 1

        count = 0
        # 0 and 1 are not prime
        for i in range(2, n):
            if vector[i]:
                count += 1

        return count


s = Solution()
assert s.countPrimes(1) == 0
assert s.countPrimes(2) == 0
assert s.countPrimes(3) == 1
assert s.countPrimes(10) == 4
assert s.countPrimes(100) == 25
assert s.countPrimes(1000) == 168
# too slow
# assert s.countPrimes(999983) == 78497

assert s.countPrimes2(1) == 0
assert s.countPrimes2(2) == 0
assert s.countPrimes2(3) == 1
assert s.countPrimes2(10) == 4
assert s.countPrimes2(100) == 25
assert s.countPrimes2(1000) == 168
assert s.countPrimes2(999983) == 78497
