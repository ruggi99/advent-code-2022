data = open("input.txt").read().splitlines()

sumcodes = 0

for i in data:
  first = i[:len(i)//2]
  second = i[len(i)//2:]
  char = ""
  for c in first:
    if c in second:
      char = c
      break
  charcode = ord(c)
  charcode -= ord("a") - 1
  if charcode < 0:
    charcode += 58
  sumcodes += charcode
  # print(c, charcode)

print(sumcodes)