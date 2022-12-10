with open("input.txt") as f:
  data = f.read().splitlines()

cycle = 0
value = 1
values = []

def cycles_to_next_checkpoint(cycle):
  if cycle <= 20:
    return 20 - cycle
  return 40 - ((cycle - 20) % 40)

for line in data:
  remaining = cycles_to_next_checkpoint(cycle)
  if remaining == 1:
    values.append((cycle + 1, value))
  if line == "noop":
    cycle += 1
  else:
    if remaining == 2:
      values.append((cycle + 2, value))
    op, quant = line.split(" ")
    cycle += 2
    value += int(quant)

print(values)

strength = 0
for cycle, value in values:
  strength += cycle * value

print(strength)