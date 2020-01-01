'''
week 2, pt 3 - divide & conquer algorithms

counting inversions in a ordered array
brute force: O(n^2) time

can we improve with recursion? yes O(nlogn)

for an inversion (i, j), i < j
    left if i & j <= n/2
    right if i & j > n/2
    split if i <= n/2 < j

first two cases can be handled recursively, split case
will require separate subroutine

high-level:
func count (array A, length N)
if N = 1 return 0
else
    x = count half 1 of A
    y = count half 2 of A
    z = count split of A
return x + y + z


key challenge is quickly counting the split inversions
have the recursive calls count inversions and also sort the array a la merge sort
when merging two sorted sub arrays, we can count split inversions at the same time

func count -> count & sort


'''