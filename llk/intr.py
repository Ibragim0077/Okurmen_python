class Test:

    def __init__(self, value):
        self.value = value


    def __add__(self, other):
        obj = Overflow(self.value + other.value)
        return obj

    def __iadd__(self, other):
        self.value += other.value
        return  self

    ob_1 = Overflow(1)
    ob_2 = Overflow(2)
    ob_3 = ob_1 + ob_2
    ob_1 += ob_2

    print(ob_3.value)
    print(ob_1.value)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        return self.age > other.age

arsen = Person()

import abc
from m math import pi


class IShape(abc.ABC):



class Circle(IShape):
    def area(self, *args, **kwargs):
        return  pi * kwargs['redis']

    def perimeter(self, *args, **kwargs)
        return kwargs['width'] * kwargs['height']

    def perimrter(self, *args, **kwargs):
        return  2 * (kwargs['width'] + kwargs['neignt'])

circle = Circle
print(circle.area(radius=5))
print(circle.perimeter(redius=5))
rect = Rectangel()
print(rect.are)

)