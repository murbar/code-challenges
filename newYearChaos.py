# https://www.hackerrank.com/challenges/new-year-chaos/problem


def minimumBribes(q):
    for i, person in enumerate(q):
        if q[i] - (i+1) > 2:
            return "Too chaotic"
            
