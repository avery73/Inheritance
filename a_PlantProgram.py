import a_PlantClass as pc

primrose = pc.Plant("Green")

sunflower = pc.Flower("Yellow", 20)
# can't create subclass without all attributes in __init__ method
# so you need the color and the petals

print(primrose.get_color())

print(sunflower.get_color())
print(sunflower.get_petals())


#print(primrose.get_petals())
