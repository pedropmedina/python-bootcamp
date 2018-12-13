# Some example from Python Cookbook

# Handle last n items in queue
from collections import deque

names = ['jane', 'john', 'johana', 'james', 'jonathan', 'jasmine']


# Read on generators here:
# https://docs.python.org/3/library/stdtypes.html#generator-types,
# https://docs.python.org/3/reference/expressions.html#yieldexpr
def search(pattern, lines):
    history = deque(maxlen=4)  # keep last 4 in queue
    for line in lines:
        if pattern in line:
            yield line, history  # return tuple using generators
        history.append(line)


for n in search('ja', names):
    print(n)

# ('jane', deque([], maxlen=4))
# ('james', deque(['jane', 'john', 'johana'], maxlen=4))
# ('jasmine', deque(['john', 'johana', 'james', 'jonathan'], maxlen=4))
