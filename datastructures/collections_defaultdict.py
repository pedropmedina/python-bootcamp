# Mapping keys to multiple values in a dictionary is possible with
# the use of another datastructure such as list, sets

# Each datastructure used as value has its advantages; list for
# example allow to keep order of item at insertion time, whereas
# sets eliminate duplicate items

# defaultdict in the collections module, allows to instantiate a dict
# with a default initial value. This is great if we know we are gonna
# need a dict of lists/sets. Knowing this, any new key in the defaultdict
# will have as its value a list/set or whathever else the defaultdict
# is initialize with. If nothing it's pass to the defaultdict, it
# will initialize with "None" as value

# More on defaultdict here:
# https://docs.python.org/3/library/collections.html#collections.defaultdict
from collections import defaultdict

people = defaultdict(list)

people['a'].append('jane')
people['a'].append('johana')

people['b'].extend(['john', 'jasmine'])

print(people)
# defaultdict(
#   <class 'list'>,
#   {
#       'a': ['jane', 'johana'],
#       'b': ['john', 'jasmine']
#   }
# )

# Each key in the people dict is defaulted to a list, but it can
# be overwritten by assigning anything else to it
people['c'] = 'String overwrites the list default value to "c" key'

print(people)
# defaultdict(
#   <class 'list'>,
#   {
#       'a': ['jane', 'johana'],
#       'b': ['john', 'jasmine'],
#       'c': 'String overwrites the list default value to "c" key'
#   }
# )


# The behavior of defaultdict can be achived with the setdefault method
# on the dict object, but the steps are less clean
d = {}
d.setdefault('a', []).append('jane')
d.setdefault('b', []).append('john')
print(d)  # {'a': ['jane'], 'b': ['john']}
