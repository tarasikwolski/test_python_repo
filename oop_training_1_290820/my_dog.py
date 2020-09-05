from oop_training_1_290820.my_animal import Animal

class MyDog (Animal):
    def __init__(self, name):
        super().__init__(name)


    def make_sound(self):
        print(f"{self.name} - Hau")
