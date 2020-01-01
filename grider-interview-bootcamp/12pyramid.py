# two sided steps


def pyramid(n):
    width = 2*n - 1
    for i in range(1, n+1):
        i = i + (i-1)
        print(('#' * i).center(width))


def pyramid2(n):
    base = 2*n - 1
    for row in range(n):
        width = row*2 + 1
        space = (base - width) // 2
        print(f'{" " * space}{"#" * width}{" " * space}')


def pyramid3(n):
    base = 2*n - 1
    mid = base // 2
    for row in range(n):
        level = ''
        for col in range(2*n - 1):
            if mid - row <= col and mid + row >= col:
                level += '#'
            else:
                level += ' '
        print(level)


def pyramidR(n, row=0, level=''):
    if n == row:
        return

    base_width = 2*n - 1
    if base_width == len(level):
        print(level)
        return pyramidR(n, row+1)

    mid = base_width // 2
    if mid - row <= len(level) and mid + row >= len(level):
        level += '#'
    else:
        level += ' '
    pyramidR(n, row, level)


pyramid(10)
pyramid2(10)
pyramid3(10)
pyramidR(10)
