import pygame
pygame.init()
pygame.font.init()

# Variables
scr = pygame.display.set_mode()
text = pygame.font.SysFont("Comic Sans MS", 50, bold=False, italic=False)
run = True
upperLimit = 20
iters = {}
size = pygame.display.get_window_size()
offset = 50
ymultiplier = 5
max = 0

# 3n+1 Loop
for i in range(1, upperLimit):
  count = 0
  num = i
  while (run == True):
    if (num == 1):
      iters[i]=count
      break
    elif (num%2 == 0):
      num = num/2
    else:
      num = num*3 + 1
    count = count+1
    if (count > max):
      max = count

values = iters.values()
values = list(values)

# Draw Graph
scr.fill('white')
for i in range(1, upperLimit):
  if (i<upperLimit-1):
    pygame.draw.lines(scr, 'black', False, ([((size[0]/upperLimit)*i)-(size[0]/upperLimit), values[i-1]*ymultiplier+(offset)], [((size[0]/upperLimit)*i), values[i]*ymultiplier+(offset)]))

# Display Text
displayText = 'Max Value: ' + str(max)
maxText = text.render(str(displayText), True, "black")
scrf = pygame.transform.flip(scr, False, True)
scr.blit(scrf , (0, 0) )
scr.blit(maxText, (200,200))
pygame.display.flip()
pygame.time.wait(5000)
