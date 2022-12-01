# const sum = function (nums: string[] | number[]) {
#   return nums.reduce((tot, cur) => tot + parseInt(cur), 0);
# };

# const text = await Deno.readTextFile('input.txt');
# const totals = text.split('\n\n').map((txt) => sum(txt.split('\n')));
# totals.sort((a, b) => b - a);
# const solutionA = totals[0];
# const solutionB = sum(totals.slice(0, 3));
# console.log({ solutionA, solutionB });

file = open("input.txt")
cals = file.read().split("\n\n")


def sum_lines(string):
    nums = string.split()
    return [int(n) for n in nums]


snacks = list(map(sum_lines, cals))
total_calories = sorted(list(map(sum, snacks)), reverse=True)
solutionA = total_calories[0]
solutionB = sum(total_calories[:3])

print(solutionA)
print(solutionB)
