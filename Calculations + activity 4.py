# do activity 4 on this one
x = float(input("Select number for x: "))
y = float(input("Select number for y: "))
cash = input("Select an operation: ")

if cash == "+":
    print(f"Addition {x + y} !")
elif cash == "-":
    print(f"Subtraction {x - y} !")
elif cash == "*":
    print(f"Multiplication {x * y} !")
elif cash == "/":
    print(f"Division {x / y} !")
else:
    print("Operation not recognized")