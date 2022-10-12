import turtle

win = turtle.Screen()
win.setup(width = 1.0, height = 1.0)

def drawEqShape(t, s, l):
  sideAngle = 360/s
  shape = 0
  while (shape < s):
    shape = shape + 1
    t.forward(l)
    t.right(sideAngle)

turt = turtle.Turtle()
turt.color('green')
turt.shape('turtle')
drawEqShape(turt, int(input('Number of Sides: ')), int(input('Side Length: ')))



win.exitonclick()