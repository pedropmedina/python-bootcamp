# Some examples taken from Python Cookbook
person_1 = {
    "name": "Bianca",
    "age": 33,
    "gender": "female",
    "address": {
        "street": "555 NW 55th St",
        "city": "Miami",
        "state": "FL",
        "country": "US",
    },
}

person_2 = {
    "name": "Luca",
    "age": 4,
    "gender": "male",
    "address": {
        "street": "555 NW 55th St",
        "city": "Miami",
        "state": "FL",
        "country": "US",
    },
}

people = [person_1, person_2]

interpolation = f"{person_1['name']} {person_2['name']}"

for key, value in person_1.items():
    print(f"{key}: {value}")

# check if key in dictionary
is_key_present = "name" in person_1
print(is_key_present)  # True

is_key_present_1 = "last_name" in person_1
print(is_key_present_1)  # False

is_value_present = 33 in person_1.values()
print(is_value_present)  # True

# == test for equality in value
# 'is' test for equality in memory
person_1_clone = person_1.copy()

print(person_1 == person_1_clone)  # True, test equality in values
print(person_1_clone is person_1)  # False, test equality in memory

# Since copy makes a shallow copy of the dict, nested dicts
# are passed by rerefence and changes to them will
# mutate that dict making changes visible in all dicts that
# reference the same nested dicts as seen below
person_1_clone["address"]["country"] = "Cuba"
print(person_1_clone)  # address: { country: Cuba }
print(person_1)  # address: { country: Cuba }

# fromkeys is use to create default dicts
person_3 = {}.fromkeys(["name", "age", "gender"], None)
print(person_3)

name = person_1.get("name")  # Bianca
non_existing = person_1.get("friends")  # None

# Since dicts don't keep order of its keys like list
# iterating over it doesn't guarantee that it'll return
# keys in order.
person_1.pop("age")  # True, returns a boolean since we already know the key

person_1.popitem()  # removes random key and returns it

person_1.update({"name": "Ana"})  # overwrites in this case name

# -------------------------------------------------------------------------
# Handling missing key in dict to avoid KeyError with get() method
jane = {'name': 'Jane', 'age': 20}

# By default the second parameter is None if no defined.
# The second parameter is returned to the user, but no changes are made
jane.get('address', 'Key does not exists!')
# ouput
# Key does not exists!

# Handling missing key with setdefult() method
# The second parameter passed to method will modify the dict adding the
# provided value to address if it does not exists. In the case, address
# exists in dict, no changes are made
jane.setdefault('address', [])
# output
# []

# -------------------------------------------------------------------------
# Using zip to invert keys and values in a dictionary
# Zip returns an iterator that can only be consumed once

# a = ['name', 'age']
# b = ['jane', 20]
# zip(a, b) -> [('name', 'jane'), ('age', 20)]

prices = {
    'ACME': 45.23,
    'APPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75,
}

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))

print(min_price)  # (10.75, 'FB')
print(max_price)  # (612.78, 'APPL')

# min and max will conduct the calculation on the item of each tuple
# in the iterable returned by zip. Min and max will never reach the second
# value in each tuple. Min and max can also perform calculation on the
# string

# We can also sort by price with the help of zip
sorted_by_price = sorted(zip(prices.values(), prices.items()))
print(sorted_by_price)

# -------------------------------------------------------------------------
# Finding commonalities in two dictionaries using "set" operations in
# their keys, values, or items
dict1 = {'x': 1, 'y': 2, 'z': 3}
dict2 = {'w': 10, 'x': 11, 'y': 2}

# Intersection
print(dict1.keys() & dict2.keys())  # {'x', 'y'}
print(set(dict1.values()) & set(dict2.values()))  # {2} had to wrap it in set
print(dict1.items() & dict2.items())  # {('y', 2)}

# Union
print(dict1.keys() | dict2.keys())  # {'w', 'x', 'z', 'y'}
print(set(dict1.values()) | set(dict2.values()))  # {1, 2, 3, 10, 11}
print(
    dict1.items() | dict2.items()
)  # {('x', 1), ('w', 10), ('z', 3), ('x', 11), ('y', 2)}

# Difference
print(dict1.keys() - dict2.keys())  # {'z'}
print(set(dict1.values()) - set(dict2.values()))  # {1, 3}
print(dict1.items() - dict2.items())  # {('z', 3), ('x', 1)}

# As explained in Python Cookbook page 16; the keys(), and items() method
# return a keys-view and items-view objects that support set operations.
# In contrast to keys() and items() methods, values() method in the
# dictionary does not support set operations as they aren't guarantee to be
# unique. To support set operations on values() method, just wrap it in
# a set()
