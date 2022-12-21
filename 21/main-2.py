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

def calc_others():
  while True:
    dict_tmp = operations.copy()
    len_before = len(dict_tmp)
    for name, rest in dict_tmp.items():
      name1, op, name2 = rest
      if name1 == "humn" or name2 == "humn":
        continue
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
    if len(operations) == len_before:
      break

def calc_humn():
  operations_copy = invert_operations()
  numbers_copy = numbers.copy()
  op_root = operations["root"]
  if op_root[0] in numbers:
    numbers_copy[op_root[2]] = numbers[op_root[0]]
  else:
    numbers_copy[op_root[0]] = numbers[op_root[2]]
  try:
    del operations_copy[op_root[0]]
    del operations_copy[op_root[2]]
  except:
    pass
  while True:
    dict_tmp = operations_copy.copy()
    len_before = len(dict_tmp)
    for name, rest in dict_tmp.items():
      name1, op, name2 = rest
      if name1 not in numbers_copy or name2 not in numbers_copy:
        continue
      del operations_copy[name]
      number1 = numbers_copy[name1]
      number2 = numbers_copy[name2]
      if op == "+":
        number = number1 + number2
      elif op == "-":
        number = number1 - number2
      elif op == "*":
        number = number1 * number2
      else:
        number = number1 // number2
      numbers_copy[name] = number
    if len(operations_copy) == len_before:
      break
  print(operations_copy)
  return numbers_copy["humn"]

def op_inv(op):
  if op == "+":
    return "-"
  if op == "-":
    return "+"
  if op == "*":
    return "/"
  return "*"

def invert_operations():
  operations_inv = {}
  oper_tmp = operations.copy()
  numbers_copy = numbers.copy()
  del numbers_copy["humn"]
  numbers_copy["root"] = 0
  for name, oper in oper_tmp.items():
    name1, op, name2 = oper
    if name1 in numbers_copy:
      if op == "/" or op == "-":
        operations_inv[name2] = [name1, op, name]
      else:
        operations_inv[name2] = [name, op_inv(op), name1]
    else:
      operations_inv[name1] = [name, op_inv(op), name2]
  return operations_inv

calc_others()

print(calc_humn())
