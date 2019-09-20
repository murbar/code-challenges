# Given three strings A, B and C. Write a function that checks whether C is an interleaving of A and B. It may be assumed that there is no common character between A and B (Please see this for an extended solution that handles common characters also), C is said to be interleaving A and B, if it contains all characters of A and B and order of all characters in individual strings is preserved. See previous post for examples.

# Solution:
# Pick each character of C one by one and match it with the first character in A. If it doesn’t match then match it with first character of B. If it doesn’t even match first character of B, then return false. If the character matches with first character of A, then repeat the above process from second character of C, second character of A and first character of B. If first character of C matches with the first character of B (and doesn’t match the first character of A), then repeat the above process from the second character of C, first character of A and second character of B. If all characters of C match either with a character of A or a character of B and length of C is sum of lengths of A and B, then C is an interleaving A and B.


# Python program to check if given string is an interleaving of
# the other two strings

# Returns true if C is an interleaving of A and B, otherwise
# returns false


def isInterleaved(A, B, C):

    # Utility variables
    i = 0
    j = 0
    k = 0

    # Iterate through all characters of C.
    while k != len(C)-1:

        # Match first character of C with first character of A,
        # If matches them move A to next
        if i < len(A) and A[i] == C[k]:
            i += 1

        # Else Match first character of C with first character
        # of B. If matches them move B to next
        elif j < len(B) and B[j] == C[k]:
            j += 1

        # If doesn't match with either A or B, then return false
        else:
            return 0

        # Move C to next for next iteration
        k += 1

    # If A or B still have some characters, then length of C is
    # smaller than sum of lengths of A and B, so return false
    if A[i-1] or B[j-1]:
        return 0

    return 1


# Driver program to test the above function
A = "AB"
B = "CD"
C = "ACBG"
if isInterleaved(A, B, C) == 1:
    print(C + " is interleaved of " + A + " and " + B)
else:
    print(C + " is not interleaved of " + A + " and " + B)
