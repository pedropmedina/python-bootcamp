# _name 'left underscore' is a convention to signify private to class
# __name__ 'dunder' signifies special build-in methods
# __name 'name mangling'
class Person:
    active_people = 0  # class attribute

    @classmethod
    def display_active_people(cls):  # class method
        return f"There are currently {cls.active_people} people."

    @classmethod
    def from_string(cls, data_str):
        first, last, age, gender = data_str.split(",")
        return cls(first, last, int(age), gender)

    def __init__(self, first, last, age, gender):
        self.first = first
        self.last = last
        self.age = age
        self.gender = gender
        Person.active_people += 1

    def remove_user(self):
        Person.active_people -= 1
        return f"{self.first} was removed."

    def full_name(self):
        return self.first + " " + self.last

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}"

    def is_senior(self):
        return self.age >= 65


print(Person.active_people)
person1 = Person("Luca", "Medina", 4, "male")
person2 = Person("Bianca", "Medina", 33, "female")
print(Person.active_people)
person1.remove_user()
print(Person.active_people)

print(Person.display_active_people())
person3 = Person.from_string("Pedro,Medina,29,male")  # using class method
print(person3.full_name())


class Pet:
    allowed = ["cat", "dog", "fish", "rat"]  # class attribute

    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You cannot have a {species} pet!")
        self.name = name
        self.species = species


cat = Pet("Blue", "cat")
dog = Pet("Orange", "dog")
