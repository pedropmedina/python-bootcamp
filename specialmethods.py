# special methods __magic__ methods
class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Human named {self.first} {self.last}."

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first="Newborn", last=self.last, age=0)
        return TypeError("You cannot add that")

    def __mul__(self, other):
        if isinstance(other, int):
            return [self for human in range(other)]
        return TypeError("Can't multiply that.")


john = Human("John", "Martin", 33)
print(len(john))

jane = Human("Jane", "Martin", 40)
print(len(jane))

newborn = john + jane
print(newborn)

twins = jane * 2
twins[0].first = "Little Jane"
print(twins)
