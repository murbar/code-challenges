def read_text_file(path):
    with open(path) as file:
        return file.read()


def sum_lines(string):
    nums = string.split()
    return [int(n) for n in nums]
