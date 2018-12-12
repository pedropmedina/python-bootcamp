# Many Examples from Python Cookbook

# Any Sequence or Iterable (lists, dicts, tuples, strings, sets) can
# be unpack into variables with the assigment operation.

t = ('John', 29, 'male', ('student', 'CS'))
name, age, gender, (occupation, major) = t

print(name)  # John
print(age)  # 29
print(gender)  # male
print(occupation)  # student
print(major)  # CS

l = ['John', 'Jane', 'Joana']
p1, p2, p3 = l

print(p1)  # John
print(p2)  # Jane
print(p3)  # Joana

s = 'Jane'
t, x, y, z = s

print(t)  # J
print(x)  # a
print(y)  # n
print(z)  # e

# We can use the _ to discard values when unpacking. Python does not
# include any special syntax for achiving this, so just use the _
l = [1, 2, 3, (33, 44, 55)]
_, _, _, important_stuff = l
print(_)  # 3
print(important_stuff)  # (33, 44, 55)

# we can unpack and an iterable of arbitrary lenght by gathering the
# rest of the values with *.
# Note: the gathered values will always be packed in a list data structure
l1 = list(range(10))
first, second, third, *rest = l1

print(first)  # 0
print(second)  # 1
print(third)  # 2
print(rest)  # [4, 5, 6, 7, 8, 9]

# we can gather an any order we want, it does not have to be the last values
*firsts, last = l1

print(firsts)  # [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(last)  # 9
