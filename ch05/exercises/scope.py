def multiply(x, times):
  newX = x
  for n in range(times-1):
    newX = newX + x
  print(newX)
  return(newX)

def exponent(x, exponent):
  newX = x
  for n in range(exponent-1):
    newX = newX*x
  print(newX)
  return(newX)

def square(x):
  newX = multiply(x, x)
  return newX
  
multiply(4, 5)
exponent(5, 2)
square(6)
