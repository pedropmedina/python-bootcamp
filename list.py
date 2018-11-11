# There're built-in functions and methods in python
names = ["Bianca", "Luca", "Philippe", "Pedro"]
print(names)

names.append("Ana")
print(names)

names.pop()
names.pop()
names.pop()
print(names)

names.append("Bianca")

print(names.count("Bianca"))  # number of ocurrances in list

names.extend(["Philippe", "Pedro"])  # takes an array of elements
print(names)

names.insert(2, "New item")
print(names)

names.clear()
print(names)

names.insert(0, "Bianca")
names.insert(0, "Luca")
print(names)

names.pop(0)
print(names)

names = ["Bianca", "Luca", "Pedro", "Philippe"]
for name in names:
    print(names.index(name))

# slicing is done with list_name[:]
new_names = names[:]  # makes a new copy of names
new_names_1 = names[:-1]  # creates new list with last item in names
new_names_2 = names[1:3]  # copies items starting at 1 up, but not including 3
new_names_3 = names[1:-1]  # copies items at index one to last items exclusive

# stepping with slicing
new_names_4 = names[::2]  # start at 0 index and go to the end in steps of 2
new_names_5 = names[::-1]  # start at the end and make a new reverse copy
new_names_6 = names[:1:-1]  # start at end and reverse up, but not including 1
new_names_7 = names[2::-1]  # start at index 2 and reveserse till index 0

# slicing and stepping can be used on strings as well
"Bianca"[1:]  # 'ianca'
"Bianca"[::-1]  # acnaiB

# swapping values in list
print("original: ", names)
names[0], names[1] = names[1], names[0]
print("swapped: ", names)

# list comprehension
nums = [1, 2, 3, 4, 5]
[name.lower() for name in names]  # ['bianca', 'luca']
[num * 2 for num in nums]  # [2, 4, 6, 8, 10]

# list comprehension with logic
nums_1 = [num * 2 for num in nums if num % 2 == 0]
print(nums_1)  # [4, 8]

nums_2 = [num * 2 if num % 2 == 0 else num / 2 for num in nums]
print(nums_2)  # [0.5, 4, 1.5, 8, 2.5]

with_vowels = "This is a great exercise"
remove_vowels = "".join([char.lower() for char in with_vowels if char not in "aeiou"])
print(remove_vowels)  # 'ths s  grt xrcs'

# list comprehension for nested lists
nums_3 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
tictactoe_board = [
    ["X" if num % 2 == 0 else "O" for num in range(1, 4)] for num in range(1, 4)
]
print(tictactoe_board)
