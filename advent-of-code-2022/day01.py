from utils import read_text_file, sum_lines

cals = read_text_file('day01input.txt').split("\n\n")
snacks = list(map(sum_lines, cals))
total_calories = sorted(list(map(sum, snacks)), reverse=True)
solutionA = total_calories[0]
solutionB = sum(total_calories[:3])

print(solutionA)
print(solutionB)
