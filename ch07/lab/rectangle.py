## Rectangle

class Rectangle:
  def __init__(self, x, y, h, w):
    if x <= 0:
      x=0
    if y <= 0:
      y=0
    if h <= 0:
      h=0
    if w <= 0:
      w=0
    self.x = int(x)
    self.y = int(y)
    self.height = int(h)
    self.width = int(w)

  def __str__(self):
    xStr = self.x
    yStr = self.y
    hStr = self.height
    wStr = self.width

    finalStr = 
    return 
    
#rect = Rectangle(-1, 1, 1, 1)
#print(rect)
