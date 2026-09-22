

try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    print(number1 / number2)

except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("you can only divide a number")
#the user could try to divide by zero which will prompt us with ZeroDivisionError
#2. the user could write a string and it cannot be converted which will result in a ValueError