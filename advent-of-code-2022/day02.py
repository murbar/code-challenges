from utils import read_text_file

# A, X = rock
# B, Y = paper
# C, Z = scissors

wins = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

draws = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

loses = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

scores = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "win": 6,
    "draw": 3,
    "lose": 0
}


def score_game(them, me):
    score = scores[me]
    if wins[them] == me:
        return score + scores["win"]
    if draws[them] == me:
        return score + scores["draw"]
    return score + scores["lose"]


def my_play(them, directive):
    if directive == "X":
        return loses[them]
    if directive == "Y":
        return draws[them]
    if directive == "Z":
        return wins[them]


my_score = 0
my_score2 = 0

throws = read_text_file('day02input.txt').split("\n")

for throw in throws:
    them, me = throw.split()
    my_score += score_game(them, me)
    my_score2 += score_game(them, my_play(them, me))

print("part 1", my_score)
print("part 2", my_score2)
