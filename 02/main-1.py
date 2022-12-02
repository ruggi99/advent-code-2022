data = open("input.txt").read().splitlines()

ROCK = 1
PAPER = 2
SCISSORS = 3
LOST = 0
DRAW = 3
WIN = 6

score = 0

for couple in data:
  if couple == "A X":
    score += DRAW
    score += ROCK
  elif couple == "A Y":
    score += WIN
    score += PAPER
  elif couple == "A Z":
    score += LOST
    score += SCISSORS
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
    score += WIN
    score += ROCK
  elif couple == "C Y":
    score += LOST
    score += PAPER
  else:
    score += DRAW
    score += SCISSORS

print(score)
