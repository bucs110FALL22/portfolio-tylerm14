# Part 1
print(10 * 5)
print(10 ** 2)
print(15 / 10)
print(15 // 10)
print(-15 // 10)
print(15 % 10)
print(10 % 15)
print(10 % 10)
print(0 % 10)
print(10 / 15)
  # this last answer repeats infinitely

# Part 2
rate = input('\nInput Current Euro -> Dollar Exchange Rate: ')
amount = input('Input Amount of Euros to Exchange: ')
total = float(rate) * float(amount)
result = (total - 3)
print('Total: $', result, '\n($3 Charged for Service Fee. Thank you!)')