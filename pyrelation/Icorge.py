from abc import ABC, abstractclassmethod


class Icorge(ABC):
    @abstractmethod
    @property
    def foo (self):
        pass

    @abstractmethod
    @foo.setter
    def foo (self, foo):
        pass