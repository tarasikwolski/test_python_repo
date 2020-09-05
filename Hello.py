from oop_training_1_290820.my_dog import MyDog
from oop_training_1_290820.my_vet import MyVet
from oop_training_figures_11_13.area_checker import AreaChecker
from oop_training_figures_11_13.figures import Rectangle, Circle, Triangle
from oop_training_figures_11_13.functions import sum_of_figures
from sda_ex_oop.cat import Cat
from oop_training_1_290820.my_cat import MyCat
from oop_training_1_290820.utilis import make_cat_list
from oop_training_1_290820.my_car import Car
from oop_training_1_290820.my_animal import Animal



def cat_creator() -> list:
    cats = []
    cat1 = Cat("Panda")
    cat2 = Cat("Filemon")
    cat1.eat_mouse()
    cats.append(cat1)
    cats.append(cat2)
    return cats


def animal_creator() -> list:
    animals = []
    cat1 = MyCat("Panda")
    cat2 = MyCat("Filemon")
    dog1 = MyDog("Ronie")
    dog2 = MyDog("Lucy")
    animals.append(cat1)
    animals.append(cat2)
    animals.append(dog1)
    animals.append(dog2)
    return animals


def main():
    # cat = Cat("Mruczek")
    # print(cat.make_sound())
    # cats = cat_creator()
    # for cat in cats:
    #     print(cat.make_sound())
    #     cat.eat_mouse()

    pass
    # wersja zajec
    cat = MyCat("Mruczek")
    print(cat.name)
    # cat.name = "Patus"
    cat.make_sound()
    print(cat.age)
    # cat.age = 2
    cat.age2(2)
    print(cat.age)
    # print("Ex2")
    # make_cat_list()
    print("Ex3")
    cat.eat_mouse()
    cat.eat_mouse()
    cat.eat_mouse()

    dog = MyDog("Ronie")
    dog.make_sound()
    animals = animal_creator()
    for animal in animals:
        animal.make_sound()

    car = Car()
    car.move()

    cat.move()
    print("Ex8")
    MyVet.say_cat_hello(cat)
    MyVet.say_dog_hello(dog)
    MyVet.say_hello(cat)

    print("Ex11-13")
    rectangle = Rectangle(12.0,10.0)
    area = rectangle.get_area()
    print(area)

    circle = Circle(3.4)
    area_circle=circle.get_area()
    print(area_circle)

    triangle = Triangle(10, 5.3)
    area_triangle=triangle.get_area()
    print(area_triangle)
    figures = [rectangle, circle, triangle]
    suma = sum_of_figures(figures)
    print(suma)

    print("Ex13")
    enough_paint = AreaChecker.check_area(180.0,figures)
    print(enough_paint)

if __name__ == "__main__":
    main()
