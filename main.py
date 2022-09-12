import pygame

pygame.init()

screen = pygame.display.set_mode()

num = 0
while (num < 1000):
  num = num + 1
  screen.fill([0, 0, 255])
  pygame.display.flip()
  screen.fill([255, 0, 0])
  pygame.display.flip()
  screen.fill([0, 255, 0])
  pygame.display.flip()