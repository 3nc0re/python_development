# Task 1
#
# Write a decorator that prints a function with arguments passed to it.
#
# NOTE! It should print the function, not the result of its execution!

def logger(func):
    def wrapper(*args):
        print(f'Function name: {func.__name__}')
        print(f'Function arguments: {args}')
        return func(*args)
    return wrapper

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

print(square_all(7, 2))