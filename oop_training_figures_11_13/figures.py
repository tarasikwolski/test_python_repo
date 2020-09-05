from oop_training_figures_11_13.figure import Figure
from math import pi


class Rectangle(Figure):
    def __init__(self, height: float, width: float):
        self.height = height
        self.width = width

    def get_area(self) -> float:
        return self.width * self.height


class Circle(Figure):
    def __init__(self, radius: float):
        self.radius = radius

    def get_area(self) -> float:
        return self.radius * pi ** 2


class Triangle(Figure):
    def __init__(self, height: float, base: float):
        self.height = height
        self.base = base

    def get_area(self) -> float:
        return self.height * self.base * 1 / 2


