# Decorator are the function which used to enhance the fumctionality 
# of the function without changing the source code. Here @ is the synatax to use decorators
def Swap(func):
    def inner(a,b,c):
        print("entered Swap func")
        if a<b:
            a,b=b,a
        return func(a,b,c)
    return inner
def helloworld(func):
    def inner(a,b,c):
        print("enter helloworld func")
        print("hello world")
        print(a,b)
        return func(a,b,c)
    return inner
@Swap
@helloworld
def div(a,b,c):
    print(a/b)

div(2,4,1)
print("!!!!!!!!!!!!!!!!!!!!")
# Above is simialr to div=Swap(helloworld(div))
div(2,4)
div=Swap(helloworld(div))
div(2,4)



def log_decorator(func):
    def wrapper(*args, **kwargs):
        # test=
        print(type(args),type(kwargs))
        print(f"Calling function '{func.__name__}' with arguments {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def add(a, b,c):
    return a + b+c

print(add(c=3,a=1, b=2))
# **kwargs is used to pass a keyworded, variable-length argument list. Here’s an example:

def func(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

func(a=1, b=2, c=3)  # prints 'a = 1', 'b = 2', 'c = 3'
# In Python, *args and **kwargs are special syntax for passing a variable number of arguments to a function.

# *args is used to pass a non-keyworded, variable-length argument list
def func(*args):
    for arg in args:
        print(arg)

func(1, 2, 3, 4)  # prints 1 2 3 4

# Python program to demonstrate working
# of map.
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
# Return double of n
def addition(n):
    print(n)
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))
