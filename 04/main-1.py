data = open("input.txt").read().splitlines()

score = 0

for line in data:
  first, second = line.split(",")
  ff, fs = map(int, first.split("-"))
  sf, ss = map(int, second.split("-"))
  if ff >= sf and fs <= ss:
    score += 1
  elif sf >= ff and ss <= fs:
    score += 1

print(score)
