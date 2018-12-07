set_one = {'one', 'two', 'three', 'four', 'five'}
set_two = {'two', 'three', 'six', 'seven'}
set_three = set(['eight', 'nine', 'two', 'ten'])
set_four = set(('eleven', 'twelve', 'thirteen', 'nine', 'ten'))

union_one = set_one | set_two
union_two = set_one.union(set_two)

intersection_one = set_three & set_four
intersection_two = set_three.intersection(set_four)

difference_one = set_one - set_two
difference_two = set_one.difference(set_two)

print('union_one: ', union_one)
print('union_two: ', union_two)

print('intersection_one: ', intersection_one)
print('intersection_two: ', intersection_two)

print('difference_one: ', difference_one)
print('difference_two: ', difference_two)

# There is not literal notation for an empty set
# using {}, will create an empty dict. In order to create
# and empty set, we must use set()
