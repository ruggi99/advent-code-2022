from collections import deque

with open("input.txt") as f:
  data = f.read().splitlines()

numbers = {}
operations = {}

for line in data:
  name, rest = line.split(": ")
  rest = rest.split(" ")
  if len(rest) == 1:
    numbers[name] = int(rest[0])
  else:
    operations[name] = rest

while True:
  dict_tmp = operations.copy()
  for name, rest in dict_tmp.items():
    name1, op, name2 = rest
    if name1 not in numbers or name2 not in numbers:
      continue
    del operations[name]
    number1 = numbers[name1]
    number2 = numbers[name2]
    if op == "+":
      number = number1 + number2
    elif op == "-":
      number = number1 - number2
    elif op == "*":
      number = number1 * number2
    else:
      number = number1 // number2
    numbers[name] = number
  if len(operations) == 0:
    break

print(numbers["root"])