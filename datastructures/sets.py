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

# Set aren't ordered just like dicts
# Set property and values are the same
# Set are good to keep track of unrepeated items
set_1 = {1, 2, 3, 4, 5, 5, 5}  # {1, 2, 3, 4, 5}
set_2 = {1, 3, 5, 6, 7}

set_1.add("Luca")
set_1.add("Bianca")

set_1.remove(1)

union_set = set_1.union(set_2)
union_set_1 = set_1 | set_2
print("union set with union method: ", union_set)
print("union set with |: ", union_set_1)

intersection_1 = set_1.intersection(set_2)
intersection_2 = set_1 & set_2
print("intersection with method: ", intersection_1)
print("intersection with &: ", intersection_2)

difference_1 = set_1.difference(set_2)
print("difference with method: ", difference_1)

# set comprehension
new_set = {x ** 2 for x in range(0, 10)}
print("new set: ", new_set)

string = "up, left, right, down"
new_set_all_vowels = len({char for char in string if char in "aeiou"}) == 5
print(new_set_all_vowels)  # False
