data = open("input.txt").read().splitlines()

sumcodes = 0

for i in range(0, len(data), 3):
  first, second, third = data[i:i+3]
  # print(first, second, third)
  char = ""
  for c in first:
    if c in second and c in third:
      char = c
      break
  charcode = ord(c)
  charcode -= ord("a") - 1
  if charcode < 0:
    charcode += 58
  sumcodes += charcode
  # print(c, charcode)

print(sumcodes)