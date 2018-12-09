# Some examples taken from Fluent Python
# Function decorators are executed as soons as the module is imported
# Decorated functions are only run when explicitly invoked
import functools
import time


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = [f'{k}={v}' for k, v in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print(f'[{elapsed:.8f}] {name}({arg_str}) -> {result}')
        return result

    return clocked


# the below example is the same as saying
# factorial = clock(factorial)
# factorial becomes the clocked function that gets invoked when factorial()
@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


print(factorial(7))

# lru = least recently used
@functools.lru_cache()
@clock
def fabonacci(n):
    if n < 2:
        return n
    return fabonacci(n - 2) + fabonacci(n - 1)


print(fabonacci(6))

# using parameterized decorators
def parents(father, mother):
    def decorator(fn):
        def child(*args, **kwargs):
            # access arguments in parents
            print(f'This are my parents: father({father}), mother({mother})')
            # run the decorated function here
            fn(*args, **kwargs)

        return child

    return decorator


@parents('John', 'Jane')  # exposes decorator function
def print_args(*args):  # becomes print_args = child(print_args)
    for arg in args:
        print(arg)


print_args(1, 2, 3, 4, 5)  # we're actually calling child

# Without the decorator, the above would look like this
parents('Jose', 'Juana')(print_args)(1, 2, 3, 4, 5)
