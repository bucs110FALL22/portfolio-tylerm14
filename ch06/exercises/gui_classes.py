class Enemy:
  def __init__(enemy, pnum, type):
    enemy.id = pnum
    enemy.type = goomba
    enemy.dead = False

class Block:
  def __init__(block, item):
    block.isBroken = False
    block.contents = item
    block.unbreakable = False

class Mystery:
  def __init__(self, item, position):
    self.contents = item
    self.position = position
    self.uses = 1
    