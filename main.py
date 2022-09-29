import random

flips = 0
streak = 0
flipsNeeded = 12

for i in range(100000):
  num = random.randrange(0,2)
  if num == (1):
    streak = streak + 1
    flips = (flips + 1)
    print("Flip:", flips, "Result:", num)
  else:
    streak = 0
    flips = flips + 1
    print("Flip:", flips, "Result:", num)
  if streak == (flipsNeeded):
    print("Got", flipsNeeded, "heads in", flips, "flips")
    break