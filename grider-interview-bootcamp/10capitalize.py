# capitalize the first letter of each word in a string


def capitalize(string):
    return string.title()


def capitalize2(string):
    words = []
    for w in string.split(' '):
        first, rest = w[0], w[1:]
        words.append(f"{first.upper()}{rest}")
    return ' '.join(words)


def capitalize3(string):
    result = ''
    for i in range(len(string)):
        if i == 0:
            result += string[i].upper()
        else:
            if result[-1] == ' ':
                result += string[i].upper()
            else:
                result += string[i]
    return result


assert capitalize('a short sentence') == 'A Short Sentence'
assert capitalize('look, it is working!') == 'Look, It Is Working!'
assert capitalize2('a short sentence') == 'A Short Sentence'
assert capitalize2('look, it is working!') == 'Look, It Is Working!'
assert capitalize3('a short sentence') == 'A Short Sentence'
assert capitalize3('look, it is working!') == 'Look, It Is Working!'
print('All tests passed!')
