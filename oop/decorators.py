from functools import wraps
from time import time


def outer(fn):
    def inner():
        print("Hello there from inner function")
        fn()

    return inner


@outer  # decorator works as if we passing the funcion
def fn_as_argument():
    print("I'm the function passed to outer as argument")


fn_as_argument()  # Then, we call the function that gets passed as arg ???

# The equivalent to the code above would be to do this:
call_inner = outer(fn_as_argument)
call_inner()

# using decorators functions with multiple arguments
def add_by_2(fn):
    @wraps(fn)  # wraps fn preserving its metadata: __doc__, __name__, etc
    def inner(*args, **kwargs):  # gather unknown number of args
        """This is just the wrapper function"""
        return fn(*args, **kwargs)

    return inner


@add_by_2
def addition(num1, num2):
    """Adds two numbers together"""
    return num1 + num2


print(addition(3, 4))

print(addition.__doc__)

# benchmarking time execution of function
def speed_test(fn):
    def wrapper(*args, **kwargs):
        wraps(fn)
        start_time = time()
        print(f"testing {fn.__name__}")
        result = fn(*args, **kwargs)
        end_time = time() - start_time
        print(f"It took {end_time} for the function to end")
        return result

    return wrapper


@speed_test
def sum_nums_generator():
    return sum(num for num in range(90_000_000))


@speed_test
def sum_nums_list():
    return sum([num for num in range(90_000_000)])


print(sum_nums_generator())
print(sum_nums_list())
