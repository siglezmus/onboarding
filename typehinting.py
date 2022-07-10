import typing


import abc

from typing import Generic, TypeVar


class Base:
    def foo(self):
        print("foo")


class Derived(Base):
    def bar(self):
        print("bar")


# can be changed to contravariant,
T_co = TypeVar('T_co', bound='Base', contravariant=True)


class Source(Generic[T_co]):
    @abc.abstractmethod
    def generate(self) -> T_co:  # Produce T_co!
        pass


class SourceBase(Source[Base]):
    def generate(self) -> Derived:  # Produce T_co!
        return Derived()


class SourceDerived(Source[Derived]):
    def generate(self) -> Derived:
        return Derived()


source: Source[Base] = SourceDerived()
print("Hello")
source.generate()
