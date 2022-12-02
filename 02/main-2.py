data = open("input.txt").read().splitlines()

ROCK = 1
PAPER = 2
SCISSORS = 3
LOST = 0
DRAW = 3
WIN = 6

score = 0

# ROCK = "A"
# PAPER = "B"
# SCISSORS = "C"

for couple in data:
  if couple == "A X":
    score += LOST
    score += SCISSORS
  elif couple == "A Y":
    score += DRAW
    score += ROCK
  elif couple == "A Z":
    score += WIN
    score += PAPER
  elif couple == "B X":
    score += LOST
    score += ROCK
  elif couple == "B Y":
    score += DRAW
    score += PAPER
  elif couple == "B Z":
    score += WIN
    score += SCISSORS
  elif couple == "C X":
    score += LOST
    score += PAPER
  elif couple == "C Y":
    score += DRAW
    score += SCISSORS
  else:
    score += WIN
    score += ROCK

print(score)
