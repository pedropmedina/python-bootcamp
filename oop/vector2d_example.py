# Some examples taken from Fluent Python

# From docs: The Python Language Reference 3. Data model
# Objects are abstraction of data. All data in Python is represented
# by objects or by relation between objects.

# Every Object has:
# 1. an identity (object's address in memory)
# 2. a type (operations supported by object)
# 3. a value (can be either mutable or immutable)

# Ways to get a string represetantion of the object
# 1. repr() -> returns a str representing object for developers purpose
# 2. str() -> returns a str representing object for user's purpose
import math
from array import array


class Vector2d:
    typecode = 'd'  # class attribute

    def __init__(self, x, y):
        self.__x = float(x)  # name mangling
        self.__y = float(y)  # both can be found in __dict__ as _Vector2d__x/y

    @property  # marks getter method of a property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    # store instance attributes in tuple instead of the default
    # dict avoiding memory overhead created by hast tables implented by dicts
    __slots__ = ('__x', '__y')

    # makes Vector2d iterable making unpacking possible
    def __iter__(self):
        return (i for i in (self.x, self.y))

    # return string interpolation with class name and values for x and y
    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}({self.x}, {self.y})'

    # Given that Vector2d is iterable, now we can use a tuple to print it
    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())  # magnitude, angle
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'  # rectangular coordinates
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    def angle(self):
        return math.atan2(self.y, self.x)


v = Vector2d(3, 5)

# -> (3, 5) as implemented by __str__
print(v)

# -> Vector2d(3.0, 5.0)  as implemented by __repr__
print(repr(v))

# test implementation of __format__
print(format(v, '.2fp'))

# unpacking possible beacuse of __iter__
x, y = v
print('this is x:', x)
print('this is y:', y)

# shows class's __dict__ {'_Vector2d__x': 3.0, '_Vector2d__y': 5.0}
# print(v.__dict__)

# Since we changed attributes of the instance to be saved in a tuple
# via the implementation of the __slots__, we no longer have
# __dict__ in the instance. Now we have access to the attrs via
# v.__slots__
print(v.__slots__)
