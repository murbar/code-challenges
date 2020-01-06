# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# permutations or a string
# initially, not sure how to tackle this one efficiently
# recursion? backtracking?

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # worst-case time and space of O(4^n)
        # potentially 4 permutations per digit in digits length n
        result = []
        digits_map = ('', '', 'abc', 'def', 'ghi', 'jkl',
                      'mno', 'pqrs', 'tuv', 'wxyz')

        def helper(current, i):
            # increment i with each recursive call
            # i == length when we're done recursing, current permutation is built
            if i == len(digits):
                result.append(current)
                return
            # get the digit at the current index
            digit = int(digits[i])
            # make recursive call for each of the chars
            for ch in digits_map[digit]:
                # add ch to current permutation and increment index
                helper(current + ch, i+1)

        # kick off
        if digits:
            # an index is more memory efficient than passing a list of remaining digits
            helper('', 0)

        return result


s = Solution()
assert s.letterCombinations('') == []
assert s.letterCombinations(
    "23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
assert s.letterCombinations(
    "5867") == ["jtmp","jtmq","jtmr","jtms","jtnp","jtnq","jtnr","jtns","jtop","jtoq","jtor","jtos","jump","jumq","jumr","jums","junp","junq","junr","juns","juop","juoq","juor","juos","jvmp","jvmq","jvmr","jvms","jvnp","jvnq","jvnr","jvns","jvop","jvoq","jvor","jvos","ktmp","ktmq","ktmr","ktms","ktnp","ktnq","ktnr","ktns","ktop","ktoq","ktor","ktos","kump","kumq","kumr","kums","kunp","kunq","kunr","kuns","kuop","kuoq","kuor","kuos","kvmp","kvmq","kvmr","kvms","kvnp","kvnq","kvnr","kvns","kvop","kvoq","kvor","kvos","ltmp","ltmq","ltmr","ltms","ltnp","ltnq","ltnr","ltns","ltop","ltoq","ltor","ltos","lump","lumq","lumr","lums","lunp","lunq","lunr","luns","luop","luoq","luor","luos","lvmp","lvmq","lvmr","lvms","lvnp","lvnq","lvnr","lvns","lvop","lvoq","lvor","lvos"]
