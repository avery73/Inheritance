
class Plant:
    def __init__(self,color):
        self.__color = color


    def get_color(self):
        return self.__color


class Flower(Plant):
    def __init__(self,color, petals):
        Plant.__init__(self,color) # first need to initalize super class

        self.__petals = petals

    def get_petals(self):
        return self.__petals
# flower subclass can call any methods in plant class 
# but not the other way around
