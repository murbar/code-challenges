# https://leetcode.com/problems/jump-game/

# feels like recursive backtracking again


# dynamic programming - keep an array of how far we can get from each point?
# cache recursive calls?

# https://leetcode.com/problems/jump-game/solution/

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # this works fine for small inputs - back to the drawing board
        # ~ O(2^n)
        def recur(jump_list):
            # how far can we jump from our current position
            distance = jump_list[0]
            # can we jump to end from here?
            if distance >= len(jump_list) - 1:
                return True

            # check again from all possible positions we can jump to
            # distance of 0 skips for loop
            for i in reversed(range(1, distance+1)):
                if recur(jump_list[i:]):
                    return True

            return False

        return recur(nums)

    def canJump2(self, nums: List[int]) -> bool:
        # "dynamic programming, top-down"
        # a greedy approach - always jump as far ahead as you can until you hit zero or end of list
        # important to keep track of dead ends along the way
        # end of list? return true, 0? backtrack to next farthest jump
        # this still fails leetcode tests - too slow for huge inputs
        # O(n^2) time?, O(n) space (n recursion depth, size n cache)
        def recur(jump_list, current_position, bad_indexes):
            # have we already checked this path and come to a dead end?
            if current_position in bad_indexes:
                return False
            # how far can we jump from our current position
            distance = jump_list[current_position]
            # can we jump to end from here?
            if distance >= len(jump_list) - current_position - 1:
                return True

            # check again from all possible positions we can jump to
            # start with farthest jump first
            # distance of 0 skips for loop
            for i in reversed(range(1, distance+1)):
                if recur(jump_list, current_position+i, bad_indexes):
                    return True

            # dead end, add current index to cache
            bad_indexes.add(current_position)
            return False

        return recur(nums, 0, set())

    def canJump3(self, nums: List[int]) -> bool:
        # "dynamic programming, bottom up"
        # process list from back -> front, eliminate recursive calls
        # memo holds what we know about each index
        # O(n^2) for each element i we inspect the nums[i] elements to find good indexes
        # O(n) space, for memo array
        UNKNOWN, GOOD = 0, 1
        memo = [UNKNOWN] * len(nums)
        # last index is good, can always get to last from last
        memo[-1] = GOOD
        # go backwards through the list, starting from second-to-last element
        for i in reversed(range(len(nums)-1)):
            # if we overshoot the end of the list, just jump to the end
            max_jump = min(i + nums[i], len(nums) - 1)

            for j in range(i+1, max_jump+1):
                if memo[j] == GOOD:
                    memo[i] = GOOD
                    break

        # print(memo)
        return memo[0] == GOOD

    def canJumpBest(self, nums: List[int]) -> bool:
        # don't need to memo at all, simply track the last known good position
        # if we reach the beginning of the list, we know there is a good path
        # O(n) time to walk the array once, O(1) space, no extra memory
        # pretty intuitive once I understood it
        # walking backward through the list, keep track of last known good index
        # start should be good when get there if there is a path
        last_position = len(nums) - 1
        # backwards through the array, starting from the last element
        for i in reversed(range(len(nums))):
            if i + nums[i] >= last_position:
                last_position = i

        # did we get to the start of the list?
        return last_position == 0


s = Solution()

# assert s.canJump([2, 3, 1, 1, 4]) == True
# assert s.canJump([3, 2, 1, 0, 4]) == False
# assert s.canJump([3, 3, 1, 0, 4]) == True
# assert s.canJump([0, 4]) == False
# assert s.canJump([0]) == True
# assert s.canJump([3, 0, 8, 2, 0, 0, 1]) == True
# assert s.canJump([
#     2, 0, 6, 9, 8, 4, 5, 0, 8, 9, 1, 2, 9,
#     6, 8, 8, 0, 6, 3, 1, 2, 2, 1, 2, 6, 5,
#     3, 1, 2, 2, 6, 4, 2, 4, 3, 0, 0, 0, 3,
#     8, 2, 4, 0, 1, 2, 0, 1, 4, 6, 5, 8, 0,
#     7, 9, 3, 4, 6, 6, 5, 8, 9, 3, 4, 3, 7,
#     0, 4, 9, 0, 9, 8, 4, 3, 0, 7, 7, 1, 9,
#     1, 9, 4, 9, 0, 1, 9, 5, 7, 7, 1, 5, 8,
#     2, 8, 2, 6, 8, 2, 2, 7, 5, 1, 7, 9, 6
# ]) == False

# assert s.canJump2([2, 3, 1, 1, 4]) == True
# assert s.canJump2([3, 2, 1, 0, 4]) == False
# assert s.canJump2([3, 3, 1, 0, 4]) == True
# assert s.canJump2([0, 4]) == False
# assert s.canJump2([0]) == True
# assert s.canJump2([3, 0, 8, 2, 0, 0, 1]) == True
# assert s.canJump2([
#     2, 0, 6, 9, 8, 4, 5, 0, 8, 9, 1, 2, 9,
#     6, 8, 8, 0, 6, 3, 1, 2, 2, 1, 2, 6, 5,
#     3, 1, 2, 2, 6, 4, 2, 4, 3, 0, 0, 0, 3,
#     8, 2, 4, 0, 1, 2, 0, 1, 4, 6, 5, 8, 0,
#     7, 9, 3, 4, 6, 6, 5, 8, 9, 3, 4, 3, 7,
#     0, 4, 9, 0, 9, 8, 4, 3, 0, 7, 7, 1, 9,
#     1, 9, 4, 9, 0, 1, 9, 5, 7, 7, 1, 5, 8,
#     2, 8, 2, 6, 8, 2, 2, 7, 5, 1, 7, 9, 6
# ]) == False


assert s.canJump3([2, 3, 1, 1, 4]) == True
assert s.canJump3([3, 2, 1, 0, 4]) == False
assert s.canJump3([3, 3, 1, 0, 4]) == True
assert s.canJump3([0, 4]) == False
assert s.canJump3([0]) == True
assert s.canJump3([3, 0, 8, 2, 0, 0, 1]) == True
assert s.canJump3([
    2, 0, 6, 9, 8, 4, 5, 0, 8, 9, 1, 2, 9,
    6, 8, 8, 0, 6, 3, 1, 2, 2, 1, 2, 6, 5,
    3, 1, 2, 2, 6, 4, 2, 4, 3, 0, 0, 0, 3,
    8, 2, 4, 0, 1, 2, 0, 1, 4, 6, 5, 8, 0,
    7, 9, 3, 4, 6, 6, 5, 8, 9, 3, 4, 3, 7,
    0, 4, 9, 0, 9, 8, 4, 3, 0, 7, 7, 1, 9,
    1, 9, 4, 9, 0, 1, 9, 5, 7, 7, 1, 5, 8,
    2, 8, 2, 6, 8, 2, 2, 7, 5, 1, 7, 9, 6
]) == False

assert s.canJumpBest([2, 3, 1, 1, 4]) == True
assert s.canJumpBest([3, 2, 1, 0, 4]) == False
assert s.canJumpBest([3, 3, 1, 0, 4]) == True
assert s.canJumpBest([0, 4]) == False
assert s.canJumpBest([0]) == True
assert s.canJumpBest([3, 0, 8, 2, 0, 0, 1]) == True
assert s.canJumpBest([
    2, 0, 6, 9, 8, 4, 5, 0, 8, 9, 1, 2, 9,
    6, 8, 8, 0, 6, 3, 1, 2, 2, 1, 2, 6, 5,
    3, 1, 2, 2, 6, 4, 2, 4, 3, 0, 0, 0, 3,
    8, 2, 4, 0, 1, 2, 0, 1, 4, 6, 5, 8, 0,
    7, 9, 3, 4, 6, 6, 5, 8, 9, 3, 4, 3, 7,
    0, 4, 9, 0, 9, 8, 4, 3, 0, 7, 7, 1, 9,
    1, 9, 4, 9, 0, 1, 9, 5, 7, 7, 1, 5, 8,
    2, 8, 2, 6, 8, 2, 2, 7, 5, 1, 7, 9, 6
]) == False
