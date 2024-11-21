from enum import Enum


class Ebaz(Enum):
    BAZ1 = ()
    BAZ2 = ()
    BAZ3 = ()

    def __new__(cls):
        newObject = object.__new__(cls)
        return newObject
