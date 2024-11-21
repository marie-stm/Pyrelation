from IFoo import IFoo
from ICorge import ICorge

class Corge(ICorge):
    foo : IFoo
    def __init__(self, foo ):
        self.__init__ = self
        self.foo = foo

        @property
        def Foo(self):
            pass