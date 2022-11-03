## Surface
from rectangle import Rectangle

class Surface:
  def __init__(self, fileName, x, y, h, w):
    self.rect = Rectangle(x, y, h, w)
    self.image = str(fileName)
  def getRect(self):
    return self.rect

#s = Surface('dnsagoisg', 3, 3, 3, 3)