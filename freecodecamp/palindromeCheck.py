'''
https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/javascript-algorithms-and-data-structures-projects/palindrome-checker

Return true if the given string is a palindrome. Otherwise, return false.

A palindrome is a word or sentence that's spelled the same way both forward and backward, ignoring punctuation, case, and spacing.

Note
You'll need to remove all non-alphanumeric characters (punctuation, spaces and symbols) and turn everything into the same case (lower or upper case) in order to check for palindromes.

We'll pass strings with varying formats, such as "racecar", "RaceCar", and "race CAR" among others.

We'll also pass strings with special symbols, such as "2A3*3a2", "2A3 3a2", and "2_A3*3#A2".
'''
import re


def is_palindrome(word):
    cleaned = re.sub(r'[^a-z0-9]', '', word, flags=re.I).lower()
    i, j = 0, len(cleaned) - 1
    while i < j:
        if cleaned[i] != cleaned[j]:
            return False
        i += 1
        j -= 1
    return True


assert is_palindrome("eye") == True
assert is_palindrome("_eye") == True
assert is_palindrome("race car") == True
assert is_palindrome("not a palindrome") == False
assert is_palindrome("A man, a plan, a canal Panama") == True
assert is_palindrome("never odd or even") == True
assert is_palindrome("nope") == False
assert is_palindrome("almostomla") == False
assert is_palindrome("My age is 0, 0 si ega ym") == True
assert is_palindrome("1 eye for of 1 eye") == False
assert is_palindrome(r"0_0 (: /-\ :) 0-0") == True
assert is_palindrome(r"five|\_/|four") == False
