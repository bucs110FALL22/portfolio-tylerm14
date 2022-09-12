import turtle

myTurtle = turtle.Turtle()
screen = turtle.Screen()

## Dimensions:
size = input("Side Length?: ")
size = float(size)
sidesNumber = input("How many sides?: ")
sidesNumber = float(sidesNumber)

sideAngle = 360/sidesNumber

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


screen.exitonclick()
