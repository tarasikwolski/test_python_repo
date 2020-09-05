from oop_training_1_290820.movable import Movable
from oop_training_1_290820.my_animal import Animal

class MyCat(Animal, Movable):
    def __init__(self,name):
        super().__init__(name)
        self.__age = 0
        self.__eat_mouse = 0


    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def age2(self, age):
        self.__age = age

    def make_sound(self):
        print(f"{self._name} - Mrau!")

    def eat_mouse(self) -> int:
        self.__eat_mouse +=1
        print(f"{self.__eat_mouse} zjadlem myszy.")
        return self.__eat_mouse

    def move(self):
        print("Ide")