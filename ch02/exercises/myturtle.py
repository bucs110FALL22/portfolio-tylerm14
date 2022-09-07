import turtle

myTurtle = turtle.Turtle()
screen = turtle.Screen()

## Hardcoded Dimensions:
size = 50
sidesNumber = 4
sideAngle = 360/sidesNumber
turn = 10

## Function to Draw Defined Shape:
def drawShape():
  shape = 0
  while (shape < sidesNumber):
    shape = shape + 1
    myTurtle.forward(size)
    myTurtle.right(sideAngle)

## Instruction:
myTurtle.shape("turtle")
myTurtle.color("purple")
drawShape()
myTurtle.penup()
myTurtle.color("red")
myTurtle.forward(60)
myTurtle.pendown()
drawShape()


screen.exitonclick()