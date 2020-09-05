class Cat():

    def __init__(self, name: str):
        super().__init__(name)
        self.__eat: int = 0

    @property
    def eat(self) -> int:
        return self.__eat

    @eat.setter
    def eat(self, val):
        self.__eat = val

    def make_sound(self) -> str:
        return f'{self.name} - Miau'

    def eat_mouse(self):
        self.eat = self.eat + 1
        print(f'Zjadłem mysz: {self.eat}')

    def move(self):
        print('ide')

