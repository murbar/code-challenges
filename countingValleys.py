# https://www.hackerrank.com/challenges/counting-valleys/problem

# var elevation
# if U elevation++
# else elevation--
# var highest elevation
# var lowest elevation
# reset highest, lowest after direction change


def countingValleys(s):
    elevation = 0
    valleys = 0
    for step in s:
        is_downhill = step == 'D'
        is_sea_level = elevation == 0
        if is_downhill and is_sea_level:
            valleys += 1
        elevation = elevation - 1 if is_downhill else elevation + 1
    return valleys


s = "UDDDUDUU"
desired_result = 1

output = countingValleys(s)
print(output)
print("Passes:", output == desired_result)
