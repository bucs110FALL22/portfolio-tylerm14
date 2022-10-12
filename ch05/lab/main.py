# :D
run = True
upperLimit = 20
iters = {}

for i in range(1, upperLimit):
  count = 0
  num = i
  while (run == True):
    if (num == 1):
      iters[i]=count
      print('Steps for',i,':', count)
      break
    elif (num%2 == 0):
      num = num/2
    else:
      num = num*3 + 1
    count = count+1

print(iters)
  