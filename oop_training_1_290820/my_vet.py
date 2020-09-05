from oop_training_1_290820.my_cat import MyCat
from oop_training_1_290820.my_dog import MyDog

class MyVet:
    @staticmethod
    def say_cat_hello(cat: MyCat):
        print(f"Hello {cat.name}!")

    def say_dog_hello(dog: MyDog):
        print(f"Hello {dog.name}!")

    @staticmethod
    def say_hello(animal):
        print(f"Hello {animal.name}!")