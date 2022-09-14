import random

num = random.randrange(1, 11)
#print(num)

guesses = 0

def guess():
  global guesses
  guessInput = int(input('Guess a number 1-10: '))
  if (guessInput > num):
    guesses = guesses + 1
    print('Too High', guesses, '/', '3 Guesses' )
    if (guesses > 2):
      print('Game Over! The Number was:', num)
    else:
      guess()
  elif (guessInput < num):
    guesses = guesses + 1
    print('Too Low', guesses, '/', '3 Guesses' )
    if (guesses > 2):
      print('Game Over! The Number was:', num)
    else:
      guess()
  elif (guessInput == num):
    print('Correct')


guess()
