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
    xStr = str(self.x)
    yStr = str(self.y)
    hStr = str(self.height)
    wStr = str(self.width)
    
    combined = [xStr, yStr, hStr, wStr]
    
    return '(xyhw): ' + str(combined)
    
#rect = Rectangle(-1, 1, 1, 1)
#print(rect)
