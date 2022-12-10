with open("input.txt") as f:
  data = f.read().splitlines()

cycle = 0
value = 1

dots = [['.' for x in range(40)] for y in range(6)]

def print_dot(cycle, value):
  row = cycle // 40
  column = cycle % 40
  if (value - 1) <= column and column <= (value + 1):
    dots[row][column] = '#'


for line in data:
  print_dot(cycle, value)
  cycle += 1
  if line != "noop":
    op, quant = line.split(" ")
    print_dot(cycle, value)
    cycle += 1
    value += int(quant)

for i in dots:
  print("".join(i))
