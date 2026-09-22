try:
    a = int(input("Tell me one number: "))
    b = int(input("Tell me anothere number: "))

    print("a/b = ", a/b)
    print("a+b", a+b)

except ValueError:
    print("Could not convert to a number.")
except ZeroDivisionError:
    print("Can't divide by zero")
except NameError:
    print("name is not defined")
except:
    print("Something went very wrong")