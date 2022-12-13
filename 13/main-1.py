import json

with open("input.txt") as f:
  data = f.read().split("\n\n")

count = 0

def check_level(_first, _second):
  for i in range(min(len(_first), len(_second))):
    first = _first[i]
    second = _second[i]
    first_is_list = isinstance(first, list)
    second_is_list = isinstance(second, list)
    if first_is_list and not second_is_list:
      second = [second]
    if not first_is_list and second_is_list:
      first = [first]
    if isinstance(first, int):
      if first < second:
        return -1
      elif first > second:
        return 1
    else:
      ret = check_level(first, second)
      if ret != 0:
        return ret
  if len(_first) < len(_second):
    return -1
  elif len(_first) > len(_second):
    return 1
  else:
    return 0


for i, line in enumerate(data):
  first, second = line.split("\n")
  first = json.loads(first)
  second = json.loads(second)
  ret = check_level(first, second)
  if ret == -1:
    count += i + 1

print(count)
