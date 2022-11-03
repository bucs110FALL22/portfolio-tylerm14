import time

#Animal Class
class Animal:
  def __init__(self, name, type, arriveDate, adoptDate):
    self.name = name
    self.type = type
    self.arriveDate = arriveDate
    self.adoptDate = adoptDate
    self.id = id(self)

#Driver
animal1 = Animal("Oreo", "Dog", "3/5/2022", time.strftime("%d/%m/%Y"))
print(animal1.name, animal1.type, animal1.arriveDate, animal1.adoptDate, animal1.id)
