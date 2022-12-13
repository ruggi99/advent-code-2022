import json
import functools

with open("input.txt") as f:
  data = f.read().splitlines()

while True:
  try:
    data.remove("")
  except:
    break

data.append("[[2]]")
data.append("[[6]]")

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

def sort_items(a, b):
  a = json.loads(a)
  b = json.loads(b)
  return check_level(a, b)

data2 = sorted(data, key=functools.cmp_to_key(sort_items))

index1 = data2.index("[[2]]") + 1
index2 = data2.index("[[6]]") + 1

print(index1 * index2)