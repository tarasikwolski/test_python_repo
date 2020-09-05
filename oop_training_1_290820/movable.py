from abc import abstractmethod, ABC
#from datetime import date as my_date

class Movable(ABC):
    @abstractmethod
    def move(self):
        pass