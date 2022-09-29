import turtle
import random

window = turtle.Screen()
window.setup(width = 1.0, height = 1.0)
turt = turtle.Turtle()
width = window.window_width()/2
height = window.window_height()/2

loop = 1
coin = 1

while (loop == 1):
  coin = random.randrange(0,2)
  if ((abs(turt.xcor()) >= width)) or ((abs(turt.ycor()) >= height)):
    print("done")
    break
  elif (coin == 0):
    turt.right(90)
    turt.forward(50)
  else:
    turt.left(90)
    turt.forward(50)


window.exitonclick()