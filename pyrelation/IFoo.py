from abc import ABC, abstractmethod

from pyrelation.Ebaz import Ebaz


class IFoo(ABC):
    @abstractmethod
    @property
    def Corge(self):
        pass

    @abstractmethod
    @property
    def Corge(self, corge):
        pass

    @abstractmethod
    def addBaz(self, baz: Ebaz):
        pass