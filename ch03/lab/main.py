import turtle #1. import modules
import random
import pygame
import math

pygame.init()

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here

michelangelo.forward(random.randrange(1,100))
leonardo.forward(random.randrange(1,100))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)


for i in range(9):
  michelangelo.forward(random.randrange(1,10))
  leonardo.forward(random.randrange(1,10))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)


# PART B - complete part B here
def drawShape(numSides, sideLength, offset, color):
  global coords
  coords = []
  for n in range(numSides):
    theta = (2.0 * math.pi * n / numSides)
    x = sideLength * math.cos(theta) + offset
    y = sideLength * math.sin(theta) + offset
    coords.append((x, y))
  pygame.draw.polygon(window, color, coords)
  pygame.display.flip()


window = pygame.display.set_mode()
window.fill("white")
pygame.display.flip()

drawShape(3, 150, 150, "red")
pygame.time.wait(1000)
window.fill("white")
drawShape(4, 150, 150, "orange")
pygame.time.wait(1000)
window.fill("white")
drawShape(6, 150, 150, "yellow")
pygame.time.wait(1000)
window.fill("white")
drawShape(9, 150, 150, "green")
pygame.time.wait(1000)
window.fill("white")
drawShape(360, 150, 150, "blue")
pygame.time.wait(1000)