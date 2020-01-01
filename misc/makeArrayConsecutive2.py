# https://app.codesignal.com/arcade/intro/level-2/bq2XnSr5kbHqpHGJC

# Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

# For statues = [6, 2, 3, 8], the output should be
# makeArrayConsecutive2(statues) = 3.

# Ratiorg needs statues of sizes 4, 5 and 7.


# sort the list then keep track of when (n + 1) - n != 1
def makeArrayConsecutive2(statues):
    statues.sort()
    ans = 0
    for n in range(len(statues)):
        try:
            diff = statues[n + 1] - statues[n]
            if diff != 1:
                ans = ans + (diff - 1)
        except:
            pass
    return ans


test_in = [6, 2, 3, 8]
test_expected_out = 3
print('Test passes:', makeArrayConsecutive2(test_in) == test_expected_out)
