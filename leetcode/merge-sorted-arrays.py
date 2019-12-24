# https://leetcode.com/problems/merge-sorted-array/
from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    m -= 1
    n -= 1
    i = len(nums1) - 1

    while i >= 0:
        if m < 0:
            nums1[i] = nums2[n]
            n -= 1
        elif n < 0:
            nums1[i] = nums1[m]
            m -= 1
        else:
            if nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1
        i -= 1


def merge2(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i1 = m - 1
    i2 = n - 1
    i = m + n - 1

    while i1 >= 0 and i2 >= 0:
        if nums1[i1] > nums2[i2]:
            nums1[i] = nums1[i1]
            i1 -= 1
        else:
            nums1[i] = nums2[i2]
            i2 -= 1
        i -= 1

    while i2 >= 0:
        nums1[i] = nums2[i2]
        i2 -= 1
        i -= 1


nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]

merge(nums1, 3, nums2, 3)
assert nums1 == [1, 2, 2, 3, 5, 6]
nums1 = [1, 2, 3, 0, 0, 0]
merge2(nums1, 3, nums2, 3)
assert nums1 == [1, 2, 2, 3, 5, 6]
