

def romanToInt(s: str) -> int:
    numerals = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }
    values = []

    while len(s):
        x, xx = s[-1:], s[-2:]
        if xx in numerals:
            values.append(numerals[xx])
            s = s[:-2]
        elif x in numerals:
            values.append(numerals[x])
            s = s[:-1]

    return sum(values)


def romanToInt2(s: str) -> int:
    total, prev = 0, 0
    numerals = {'I': 1, 'V': 5, 'X': 10,
                'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in s[::-1]:          # rev the s
        if numerals[i] >= prev:
            # sum the value if previous value same or more
            total += numerals[i]
        else:
            # substract when value is like "IV" --> 5-1, "IX" --> 10 -1 etc
            total -= numerals[i]
        prev = numerals[i]
    return total


assert romanToInt("MCMXCIV") == 1994
assert romanToInt2("MCMXCIV") == 1994
