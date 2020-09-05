from abc import ABC
class Animal(ABC):

    def __init__(self, name):
        self._name = name

    @property
    def name(self) -> str:
        return self._name