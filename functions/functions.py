# keyword arguments allows to assign value to arguments
# regardless of the order.


def say_hi(first_name, last_name):
    return f"Hi {first_name} {last_name}"


# Now we can pass the arguments in any order
greeting = say_hi(last_name="Medina", first_name="Luca")
print(greeting)  # Hi Luca Medina

# default parameters. This is similar to JS


def say_hello(name="Luca"):
    return f"Hello there {name}"


print(say_hello())  # Hello there Luca
print(say_hello("Bianca"))  # Hello there Bianca

# scope
# We can tell python to target a global variable outside the
# scope of a function by using the keyword 'global'
# Even though the 'global' keyword exist, we can approach
# variables the same way we do in javascript as long as we
# are not completing any operations on them other than
# retuning them.
# The reason for this, is that since python does not uses
# keyword to define its variables if we complete operation
# such as for example addition on total in the function
# below we will be adding to total which has not been
# defined in the eyes of python
total = 0


def increment():
    global total  # use global total variable
    total += 1
    return total


print(increment())  # 1
print(increment())  # 2
print(increment())  # 3

# nonlocal keyword is use to manipulate variables
# within the outer functions scope. Important when
# using closure


def outer():
    """Increses counter in the parent function's scope using closure"""
    counter = 0

    def inner():
        nonlocal counter  # counter in the parent scope
        counter += 1
        return counter

    return inner


# Another thing that we cannot do in python is return
# something like this: return counter += 1 as it freaks out
# thinking that wee are returning and completing an assignment
# operation at the same time. This behavior is fine in
# Javascript, but not in python

# This is how we access the documation for a function __doc__
# To set the documentation to a function we use """ """ as
# seen above in the outer function
# Increses counter in the parent function's scope using closure
print(outer.__doc__)

# Gathering is achive with the * symbol. The is the equivalent
# to rest ... in javascript. Pythons returns the args in a
# tuple data structure


def sum_all_nums(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


print(sum_all_nums(1, 2, 3, 4))  # 10

# We can also gather arguments with ** double asterisk in
# The main diference with a single * is that python
# will  return a dictionaty {} instead of a tuple
# This approach is useful when passing keywords to
# arguments to functions


def fav_colors(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, " -> ", v)


fav_colors(bianca="red", luca="blue", philippe="green")

# Unpacking is the equivalent to spread in Javascript and
# it is pretty much use in the same context. The big
# difference is that we use * instead of ...
names = ["Bianca", "Luca", "Pedro"]
mixed_array = [1, 2, 3, *names]
print(mixed_array)  # [1, 2, 3, "Bianca", "Luca", "Pedro"]

mixed_array_1 = [*names, 1, 2, 3]
print(mixed_array_1)

# Just as we unpack with *, we can use ** to unpack
# dictionaries
person = {"name": "Pedro", "age": 29}
add_to_person = {**person, "gender": "male"}
print(add_to_person)  # {"name": "Pedro", "age": 29, "gender": "male"}

# lambda functions
# lambda functions are the equivalent of arrow functions in JS


def func(num):
    return num * num


print(func(3))  # 9

func_1 = lambda num_1: lambda num_2: num_1 * num_2

print(func_1(3)(4))  # 12

# map
numbers = [1, 2, 3, 4, 5, 6]
doubles = list(map(lambda x: x * 2, numbers))  # map returns an map object
print(doubles)  # [2, 4, 6, 8, 10, 12] we use list() on map object

# filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6]

names_with_b = list(
    map(
        lambda name: name.upper(),
        filter(lambda name: name[0].lower() == "b", names),
    )
)
print(names_with_b)

# Built-in functions:

# all
# Returns True if all elements are thruthy, else returns False
names_1 = ["Bianca", "Blanca", "Bana", "Banana"]
names_2 = ["Bianca", "Blanca", "Bana", "Tana"]

names_with_B = [name[0] == "B" for name in names_1]
most_names_with_B = [name[0] == "B" for name in names_2]

print(names_with_B)  # [True, True, True, True]
print(most_names_with_B)  # [True, True, True, False]

print(all(names_with_B))  # True
print(all(most_names_with_B))  # False

# any
# Returns True if any element is thruthy
print(any(num % 2 == 0 for num in [1, 2, 3, 4]))  # True

# sorted
# Sorts and returns new list. It works with lists and tuples
numbers_1 = [1, 66, 534, 33, 2, 5]
songs = [
    {"title": "Black hole sun", "artist": "Soundgarden", "playcount": 44},
    {"title": "Black", "artist": "Pearl Jam", "playcount": 134},
    {"title": "One", "artist": "Metallica", "playcount": 3},
]

print(sorted(numbers_1))  # [1, 2, 5, 33, 66, 534]
print(sorted(numbers_1, reverse=True))  # [534, 66, 33, 5, 2, 1]
print(numbers_1)  # [1, 66, 534, 33, 2, 5]

# sorted_by_playcount = sorted(songs, key=lambda song: song["playcount"])
sorted_by_playcount = sorted(
    songs, key=lambda song: song["playcount"], reverse=True
)
print(sorted_by_playcount)

# min and max
# we can pass in list, dicts, tuples, string, numbers
print(min(28, 323, 1, 24, 36))
print(max(28, 323, 1, 24, 36))
print(max(numbers_1))
print(min((1, 2, 3, 4, 6)))
print(min("hello"))
print(max(songs, key=lambda song: len(song["title"])))
print(max(songs, key=lambda song: len(song["title"]))["title"])

# reversed
# Retuns a new reversed object without mutating the original
print(list(reversed(numbers_1)))
