# You are given a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates in the list. One of the integers is missing in the list. Write an efficient code to find the missing integer.

# sum formula
# 1. Get the sum of numbers which is total = n*(n+1)/2
# 2. Subtract all the numbers from sum and
#    you will get the missing number


def getMissingNo(nums, n):
    i, total = 0, 1

    for i in range(2, n + 2):
        total += i
        total -= nums[i - 2]
    return total


# Driver Code
arr = [1, 2, 3, 5]
print(getMissingNo(arr, len(arr)))
