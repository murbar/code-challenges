# https://www.hackerrank.com/challenges/sparse-arrays/problem


def matchingStrings(strings, queries):
    results = [0] * len(queries)
    for s in strings:
        for i, q in enumerate(queries):
            if s == q:
                results[i] += 1

    return results


# tests
test_strings = [
    "abcde",
    "sdaklfj",
    "asdjf",
    "na",
    "basdn",
    "sdaklfj",
    "asdjf",
    "na",
    "asdjf",
    "na",
    "basdn",
    "sdaklfj",
    "asdjf"
]
test_queries = [
    "abcde",
    "sdaklfj",
    "asdjf",
    "na",
    "basdn"
]
expected_output = [1, 3, 4, 3, 2]
print('Passes:', matchingStrings(test_strings, test_queries) == expected_output)
