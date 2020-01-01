# print a step shape with N levels using # character
# pad upper steps with spaces


def steps(n):
    for i in range(1, n+1):
        print(('#' * i).ljust(n))


def steps2(n):
    for row in range(n):
        stair = ''
        for col in range(n):
            if col <= row:
                stair += '#'
            else:
                stair += ' '
        print(stair)


def steps3(n, row=0, stair=''):
    if n == row:
        return

    if n == len(stair):
        print(stair)
        return steps3(n, row+1)

    if len(stair) <= row:
        stair += '#'
    else:
        stair += ' '
    steps3(n, row, stair)


steps(10)
steps2(10)
steps3(10)
