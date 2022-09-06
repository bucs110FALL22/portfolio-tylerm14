import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)

classes_per_week = 3
cost_per_class = (cost_per_week / classes_per_week)
print("Cost per class:", cost_per_class, type(cost_per_class))
#Part B
devicesList = ["Phone", "PC", "Tablet", "Laptop", "TV"]

randDevice = random.choice(devicesList)
print("Random Device Chosen:", randDevice)