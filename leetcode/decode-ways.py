''' https://leetcode.com/problems/decode-ways/
intuition:      dynamic programming, recursion
                for each element in array, ways is current + ways from last element
                similar to climbing stairs problem
                use results of sub-problems to solve
input:          non-empty string of digits
output:         int, number of ways to decode input string
constraints:    
edge cases:     0 does not map to a letter, but 10 & 20 does
                if digits starts with 0, can't be decoded
time:           O(2^n) without memo, O(n) with memo
space:          O(n), twice as much for DP version
'''


class Solution:
    def numDecodings(self, s: str) -> int:
        # works but makes many duplicate calculations
        def count_ways(digits, last_k):
            if last_k == 0:
                return 1

            start = len(digits) - last_k
            if digits[start] == '0':
                return 0

            ways = count_ways(digits, last_k-1)
            if last_k >= 2 and int(digits[start:start+2]) <= 26:
                ways += count_ways(digits, last_k-2)

            return ways

        return count_ways(s, len(s))

    def numDecodingsDP(self, s: str) -> int:
        # we can optimize by caching intermediate results

        # recursive helper
        def count_ways(digits, last_k, memo):
            # only 1 way to decode an empty string
            if last_k == 0:
                return 1

            start = len(digits) - last_k
            # 0 doesn't map to a letter (only values 1-26)
            if digits[start] == '0':
                return 0

            # have we already solved for this k?
            if memo[last_k] != None:
                return memo[last_k]
            # first digit will be 1-9
            ways = count_ways(digits, last_k-1, memo)
            # if first two digits are 10-26, add that to ways
            if last_k >= 2 and int(digits[start:start+2]) <= 26:
                ways += count_ways(digits, last_k-2, memo)

            # cache this result and return
            memo[last_k] = ways
            return ways

        memo = [None] * (len(s) + 1)
        return count_ways(s, len(s), memo)

    def numDecodingsDP2(self, s: str) -> int:
        # memoized, without recursion
        if s[0] == '0':
            return 0

        memo = [0] * (len(s) + 1)
        memo[0] = 1
        memo[1] = 1
        for i in range(2, len(s) + 1):
            one_digit = int(s[i-1:i])
            two_digits = int(s[i-2:i])
            if one_digit != 0:
                memo[i] += memo[i-1]
            if two_digits >= 10 and two_digits <= 26:
                memo[i] += memo[i-2]

        return memo[-1]

    def numDecodingsDP3(self, s: str) -> int:
        # memoized, iterative, O(1) space
        # if we are only using the last two values in the memo array, we can just
        # use two vars and update as we go, save the space for the array

        if s[0] == '0':
            return 0

        # store results as we go
        prev_prev = 1
        prev = 1

        for i in range(2, len(s) + 1):
            current = 0
            last_digit = int(s[i-1])
            last_two_digits = int(s[i-2:i])

            if last_digit != 0:
                current += prev
            if last_two_digits >= 10 and last_two_digits <= 26:
                current += prev_prev

            prev_prev = prev
            prev = current

        return prev


s = Solution()
assert s.numDecodings("12") == 2
assert s.numDecodings("226") == 3
assert s.numDecodings("128562335") == 4
assert s.numDecodings("011") == 0
assert s.numDecodings("9011") == 0

assert s.numDecodingsDP("12") == 2
assert s.numDecodingsDP("226") == 3
assert s.numDecodingsDP("128562335") == 4
assert s.numDecodingsDP("011") == 0
assert s.numDecodingsDP("9011") == 0
assert s.numDecodingsDP("1285623351285623351208562335") == 32

assert s.numDecodingsDP2("12") == 2
assert s.numDecodingsDP2("226") == 3
assert s.numDecodingsDP2("128562335") == 4
assert s.numDecodingsDP2("011") == 0
assert s.numDecodingsDP2("9011") == 0
assert s.numDecodingsDP2("1285623351285623351208562335") == 32

assert s.numDecodingsDP3("12") == 2
assert s.numDecodingsDP3("226") == 3
assert s.numDecodingsDP3("128562335") == 4
assert s.numDecodingsDP3("011") == 0
assert s.numDecodingsDP3("9011") == 0
assert s.numDecodingsDP3("1285623351285623351208562335") == 32
assert s.numDecodingsDP3("128562335128562003351208562335") == 0
