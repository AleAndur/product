#Program number 3: Create a Python program that converts temperatures between Celsius and Kelvin.
#     Hint:
#     Kelvin = Celsius + 273.15
#     Celsius = Kelvin− 273.15
#     User must be able to choose the type of conversion.
#     Also, the program must be able to convert from Celsius to Kelvin and Celsius to
#     Kelvin


temperature = float(input("What is the temperature you desire to convert? ..."))
conversion = int(input("Choose a conversion: \n 1. Celsius to Kelvin \n 2. Kelvin to Celsius \n..."))
if conversion == 1:
	kelvin = temperature + 273.15
	print(f"The result is {kelvin} kelvin!")
elif conversion == 2:
	celsius = temperature - 273.15
	print(f"The result is {celsius} celsius!")
else:
	print("Select one or two.Try again!")

