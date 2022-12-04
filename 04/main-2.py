data = open("input.txt").read().splitlines()

score = 0

for line in data:
  first, second = line.split(",")
  ff, fs = map(int, first.split("-"))
  sf, ss = map(int, second.split("-"))
  if fs >= sf and ff <= ss:
    score += 1

print(score)
