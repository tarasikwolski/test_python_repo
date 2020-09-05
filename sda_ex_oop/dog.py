class Dog():

    def __init__(self, name):
        super().__init__(name)  # jesli dziedziczymy i klasa Ojciec ma to pole to przekazujemy przez super
        # self. name = name # jesli nie dziedziczymy to wyglada to tak

    def dog_creator() -> list:
        dogs = []
        dog1 = Dog("Dog1")
        dog2 = Dog("Dog2")
        dog1.make_sound()
        dogs.append(dog1)
        dogs.append(dog2)
        return dogs

    def make_sound(self) -> str:
        return f'{self.name} - Hau'