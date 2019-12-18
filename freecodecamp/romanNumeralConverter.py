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


def convert_to_roman(n):
    roman = ''

    for num, val in numerals.items():
        while n >= val:
            roman += num
            n -= val

    return roman


assert convert_to_roman(2) == "II"
assert convert_to_roman(3) == "III"
assert convert_to_roman(4) == "IV"
assert convert_to_roman(5) == "V"
assert convert_to_roman(9) == "IX"
assert convert_to_roman(12) == "XII"
assert convert_to_roman(16) == "XVI"
assert convert_to_roman(29) == "XXIX"
assert convert_to_roman(44) == "XLIV"
assert convert_to_roman(45) == "XLV"
assert convert_to_roman(68) == "LXVIII"
assert convert_to_roman(83) == "LXXXIII"
assert convert_to_roman(97) == "XCVII"
assert convert_to_roman(99) == "XCIX"
assert convert_to_roman(400) == "CD"
assert convert_to_roman(500) == "D"
assert convert_to_roman(501) == "DI"
assert convert_to_roman(649) == "DCXLIX"
assert convert_to_roman(798) == "DCCXCVIII"
assert convert_to_roman(891) == "DCCCXCI"
assert convert_to_roman(1000) == "M"
assert convert_to_roman(1004) == "MIV"
assert convert_to_roman(1006) == "MVI"
assert convert_to_roman(1023) == "MXXIII"
assert convert_to_roman(2014) == "MMXIV"
assert convert_to_roman(3999) == "MMMCMXCIX"
