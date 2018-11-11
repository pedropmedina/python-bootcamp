# there are integer and floating points in python

# if any type of a calculation is a float, python
# will output (favor) a float. So 1 + 1.0 = 2.0

# In python division always returns a 'float', unless
# we use the integer (floored) division '//'


def hello(name):
    return 'Hello there' + ' ' + name


def addBy2(x):
    return x + 2


def mulBy2(x):
    return x * 2


def run(fn1, fn2):
    def closure(x):
        return fn1(fn2(x))
    return closure


print(run(addBy2, mulBy2)(3))

'''
Data types:
1. int - 6
2. float - 7.5
3. str - 'hello there'
4. bool - True or False (uppercased)
5. list - [1, 2, 3, 4]
6. dict - {'name: 'Pedro', 'age': 29}
7. None - same as js's null
'''
