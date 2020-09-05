from datetime import date

class Person:
    def __init__(self, name: str, surname: str, DOB: date):
        self._name=name
        self._surname = surname
        self._DOB = DOB

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value: str):
        self._surname = value

    @property
    def DOB(self):
        return self._DOB

    @DOB.setter
    def DOB(self, value: date):
        self._DOB = value
