with open("input.txt") as f:
  data = f.read().splitlines()

total = 0
for snafu in data:
  snafu_len = len(snafu)
  number = 0
  for i in range(snafu_len):
    power = snafu_len - i - 1
    subtotal = 5 ** power
    char = snafu[i]
    if char == "=":
      subtotal *= -2
    elif char == "-":
      subtotal *= -1
    else:
      subtotal *= int(char)
    number += subtotal
  total += number

rem = total
snafu = ""
while True:
  mod = rem % 5
  rem = round(rem / 5)
  if mod < 3:
    snafu = str(mod) + snafu
  elif mod == 3:
    snafu = "=" + snafu
  else:
    snafu = "-" + snafu
  if rem == 0:
    break

print(total)
print(snafu)