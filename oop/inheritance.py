class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self._age = age  # convention for private

    def __repr__(self):
        return f"{self.first} is a human."

    # def get_age(self):
    #     return self._age

    # def set_age(self, new_age):
    #     if new_age >= 0:
    #         self._age = new_age
    #     else:
    #         self._age = 0

    @property  # works as a getter
    def age(self):
        return self._age

    @age.setter  # works as a setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("Age can't be negative")

    @property
    def full_name(self):
        return f"{self.first} {self.last}"


# jane = Human("Jane", "Jones", 32)
# print(jane.age)  # getter
# jane.age = 55  # setter
# print(jane.age)
# print(jane.full_name)


class Student(Human):
    def __init__(self, first, last, age, school, grade):
        super().__init__(first, last, age)
        self.school = school
        self.grade = grade

    def info(self):
        return f"{self.first} is atteding {self.school} for {self.grade}."


luis = Student("Luis", "Manson", 5, "Genius Institue", "Pre-k")

print(luis.info())
