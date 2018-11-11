# tuples are immutable as oposite of dicts and list
# tuples are also faster than lists
# We can nest tuples
# Also we can slice tuples with [:]
alphabet = ("a", "b", "c", "d", "e", "...")

alphabet[0]  # "a"

print(type(alphabet))

# tuples can be used as a property to a dic
dictionary = {
    ("Bianca", "Medina"): "CEO",
    ("Pedro", "Medina"): "CTO",
    ("Luca", "Medina"): "CFO",
}

print(dictionary[("Bianca", "Medina")])

# iterating over tuples is the same as list
for letter in alphabet:
    print(letter)

#######################################################
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
