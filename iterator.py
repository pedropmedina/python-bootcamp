# iterables:
# list [1, 2, 3, 4, 5]
# str 'hello'
# tuple (1, 2, 3, 4)
# set {1, 2, 3, 4}
# dict {"name": "Bianca", "age": 33}

# iterator:
# Any iterable enclosed in iter,
# that then, gets call with next()
# until it reaches the error StopIteration

i = iter([1, 2, 3, 4])
print(next(i))  # 1
print(next(i))  # 2
print(next(i))  # 3
print(next(i))  # 4
# print(next(i))  # StopIteration

# custom for
def my_for(iterable, fn):
    iterator = iter(iterable)
    while True:
        try:
            fn(next(iterator))
        except StopIteration:
            break


print(my_for([1, 2, 3, 4, 5], print))

# custom iterator in class
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration


for x in Counter(50, 70):
    print(x)
