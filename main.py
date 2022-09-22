import random
import pygame
import math

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