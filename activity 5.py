number = int(input("Please insert a number: "))

if number > 100:
    print("Big number!")
elif number > 49:
    print("Medium number!")
elif number > 1:
    print("Small number!")
else:
    print("Negative number!")
