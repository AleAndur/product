def calc_react_area(length, width):
    area = length * width
    print(area)

calc_react_area(10, 4)

def test():
    x = 2
    y = 3
    z = x + y
    print(z)
test()

def test_two():
    x = float(input("Please give me a number to add: "))
    y = float(input("Please give me a number to add: "))
    z = x + y
    print(z)

test_two()

def greet(name, age):
     name = input("Tell me your name: ...")
     print(f"Good morning {name} ! You are {age} years old, correct?")

greet(str, 22)