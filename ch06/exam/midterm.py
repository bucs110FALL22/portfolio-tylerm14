import turtle

##TRY "RAINBOW" AS THE COLOR :D

def main():
  turt = turtle.Turtle()
  screen = turtle.Screen()
  colorsRainbow = ["red", "orange", "yellow", "green", "blue", "purple"]

  def askColor():
    colorInput = input('Color?: ')
    return colorInput.lower()
  def askSides():
    try:
      sidesInput = int(input('Sides Number?: '))
      return sidesInput
    except:
      print('not a valid number')
      exit()
  def askSize():
    try:
      sizeInput = int(input('Initial Side Length?: '))
      return sizeInput
    except:
      print('not a valid number')
      exit()
  
  def draw(sidesNumber, size, chosenColor):
    sideAngle = 360/sidesNumber
    screen.setup(width = 1.0, height = 1.0)
    turt.hideturtle()
    screen.bgcolor('black')
    newSize = size
    color = 0
    
    for loops in range(1, int(size/2)):
      if (chosenColor == 'rainbow'):  
        if (color > len(colorsRainbow)-1):
          color = 0
        turt.color(colorsRainbow[color])
        color = color+1
      else: 
        try:
          turt.color(chosenColor)
        except:
          print('not a valid color')
          exit()
      for x in range(0, sidesNumber):
        turt.forward(newSize*0.95)
        newSize = newSize*0.95
        turt.right(sideAngle)
  
  draw(askSides(), askSize(), askColor())
  print('done')
  
  screen.exitonclick()

main()
