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
