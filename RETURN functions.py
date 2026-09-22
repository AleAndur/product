x = int(input("enter the value of x : ")) # global variable


def square(x):
    r = x * x # local variable
    return r


print(f"{square(x)} is the square of {x} square")

#global variables are outside of functions and local variables are inside functions.
