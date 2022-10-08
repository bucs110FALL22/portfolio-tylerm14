import pygame
import math
import random

p1score = 0
p2score = 0

pygame.init()

#Setup Dartboard
screen = pygame.display.set_mode()
size = pygame.display.get_window_size()
screen.fill("white")
pygame.draw.circle(screen, "pink", [size[0]/2, size[1]/2], size[1]/2)
pygame.draw.circle(screen, "black", [size[0]/2, size[1]/2], size[1]/2, width=1)
pygame.draw.line(screen, "black", [size[0]/2 - size[1]/2, size[1]/2], [size[0]/2 + size[1]/2, size[1]/2], width=1)
pygame.draw.line(screen, "black", [size[0]/2, size[1]], [size[0]/2, 0], width=1)
pygame.display.flip()

#Print Score
def printScore():
  print("Player 1 Score:", p1score )
  print("Player 2 Score:", p2score )


#GAMING
for i in range(10):
  print('Player 1 Throws...')
  throw = [ random.randrange(0, size[0]), random.randrange(0, size[1]) ]
  pygame.draw.circle(screen, "blue", [throw[0], throw[1]], 7)
  distance_from_center = math.hypot((size[0]/2)-throw[0], (size[1]/2)-throw[1])
  inCircle = distance_from_center <= size[1]/2
  pygame.display.flip()
  if (inCircle == True):
    p1score = p1score+1
    print('Hit!')
    printScore()
  else:
    print('Miss')
    printScore()
  pygame.time.wait(500)
  
  print('Player 2 Throws...')
  throw = [ random.randrange(0, size[0]), random.randrange(0, size[1]) ]
  pygame.draw.circle(screen, "red", [throw[0], throw[1]], 7)
  distance_from_center = math.hypot((size[0]/2)-throw[0], (size[1]/2)-throw[1])
  inCircle = distance_from_center <= size[1]/2
  pygame.display.flip()
  if (inCircle == True):
    p2score = p2score+1
    print('Hit!')
    printScore()
  else:
    print('Miss')
    printScore()
  pygame.time.wait(500)

#Final Scoring
print('\nFinal Scores:')
printScore()
if (p1score > p2score):
  print('Player 1 Wins!')
elif (p1score == p2score):
  print('Tie!')
else:
  print('Player 2 Wins!')

pygame.time.wait(10000)
