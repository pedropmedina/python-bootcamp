# Dictionaries by default don't keep track of the order in which
# entries are added for efficiency reasons as they implement
# a hash table in under the hood.

# The OrderedDict in the collections module keeps order of the keys
# at insertion time. Under the hood, the a doubly linked list is implemented
# which appends each new item to the of the list. The fact that it
# uses a doubly linked list, makes the OrderedDict a bit more
# heavy in memory consumption. MORE ON THIS: Python Cookbook page 13

# If a new entry ovewrites an existing entry, the original insertion
# position is left unchanged. This is the expected behavior

# Equality test between OrderedDict objects are order-sensitive, it is
# implemented as list(od1.items()) == list(od2.items())

# Now equality test between an OrderedDict object an any other Mapping
# object is order-insensitive meaning we can use OrderedDict as a replacement
# to dicts and it won't break anything


# More on OrderedDict here:
# https://docs.python.org/3/library/collections.html#ordereddict-objects

# More on JSON here:
# https://docs.python.org/3/library/json.html
import json
from collections import OrderedDict

person = OrderedDict()

person['name'] = 'jane'
person['age'] = 20
person['gender'] = 'female'

print(person)
# OrderedDict([('name', 'jane'), ('age', 20), ('gender', 'female')])

# Serialize person maintaining the order
print(json.dumps(person))
# {"name": "jane", "age": 20, "gender": "female"}
