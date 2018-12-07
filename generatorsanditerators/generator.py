def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1


counter = count_up_to(3)
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3
# print(next(counter)) # StopIterator

# infinity generator
def current_beat():
    nums = (1, 2, 3, 4)
    i = 0
    while True:
        if i >= len(nums):
            i = 0
        yield nums[i]
        i += 1


beat_counter = current_beat()
print(next(beat_counter))  # 1
print(next(beat_counter))  # 2
print(next(beat_counter))  # 3
print(next(beat_counter))  # 4
print(next(beat_counter))  # 1
print(next(beat_counter))  # 2
print(next(beat_counter))  # 3 ...

# fibonnaci sequence with generators. Generators consume less memory
# when iterating over a large set of data
def fibonacci(max):
    x, y = 0, 1
    count = 0
    while count < max:
        x, y = y, x + y
        yield x
        count += 1


# for n in fibonacci(1000000):
#     print(n)

# generator expressions. Its biggest difference with list expression,
# is the use of () versus []
generator_expression = (num for num in range(1, 10))
print(next(generator_expression))  # 1
print(next(generator_expression))  # 2
print(next(generator_expression))  # 3
print(next(generator_expression))  # 4 ...

print(sum(num for num in range(1, 10)))  # 45
