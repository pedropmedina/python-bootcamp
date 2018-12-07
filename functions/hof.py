# Higher order functions are functions that take a function
# as an argument or return a function as a result
# Some example of HOF are map, filter, reduce, sorted
names = ['bianca', 'jane', 'johana', 'anna', 'maria', 'juana']

sorted_by_len = sorted(names, key=len)
# ['jane', 'anna', 'maria', 'juana', 'bianca', 'johana']

cap_names = map(lambda name: name.capitalize(), names)
# ['Bianca', 'Jane', 'Johana', 'Anna', 'Maria', 'Juana']


# Function that returns another function
def outter(a):
    def inner(b):
        return a + b

    return inner


print(outter(5)(6))  # 11
