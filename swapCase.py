def swap_case(s):
    chars = [c for c in s]
    new_chars = []
    for c in chars:
        if c.isupper():
            new_chars.append(c.lower())
        else:
            new_chars.append(c.upper())
    return ''.join(new_chars)
