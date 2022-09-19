import random

num = random.randrange(1, 11)
#print(num)

guesses = 3
guessNumber = guesses

for i in range(guesses):
  guessInput = int(input('Guess a number 1-10: '))
  if (guessInput > num):
    guessNumber = guessNumber - 1
    print('Too High', guessNumber, '/', guesses, 'Guesses Left' )
  elif (guessInput < num):
    guessNumber = guessNumber - 1
    print('Too Low', guessNumber, '/', guesses, 'Guesses Left' )
  elif (guessInput == num):
    print('Correct!')
    break
