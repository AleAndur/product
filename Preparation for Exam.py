
''''
Variables, Data Types & Casting
1. Ask the user for a product name, price, and quantity. Calculate and print the total cost, formatted to 2 decimal places using an f-string.


2. Write a program that stores your age as a string, then casts it to an int and prints type() before and after casting.

3. Ask for a temperature in Celsius (as input) and convert it to Fahrenheit, printing both values with labels.
4. A staff member is assigned a bonus rating ranging from 1 to 4. The bonus awarded depends on the rating as follows:
Rating 1: 20% of the basic salary
Rating 2: 15% of the basic salary
Rating 3: 10% of the basic salary
Rating 4: 5% of the basic salary

Write a Python program that:
Takes the staff member’s basic salary and bonus rating (1–4) as input.
Calculates the bonus amount based on the given rating.
Displays the calculated bonus amount.
5. In the UK, the personal tax-free allowance is £12,570. Income above this threshold is taxed according to the following bands:
20% (basic rate): Taxable income up to £50,250
40% (higher rate): Taxable income from £50,251 to £125,140
45% (additional rate): Taxable income above £125,140
Write a Python program that:
Takes the user’s gross annual income as input.
Calculates the total income tax payable, considering the tax-free allowance.
Applies the correct tax rates to the appropriate portions of income.
Displays the total tax amount.
Additional requirements:
Ensure the program correctly handles incomes below the tax-free allowance (no tax payable).
Clearly separate calculations for each tax band.

'''
#1.
product_name = input("Tell me the product name: ")
price = float(input("Tell me the price: "))
quantity = int(input("Tell me the quantity: "))

total = price * quantity
print(f"The total cost for {product_name} is {total:.2f} £.")

#2.
age = str(input("Tell me your age."))

print(type(age))

age_two = int(age)

print(type(age_two))

#3.
temperature = int(input("Give me a temperature in Celsius: "))

fahrenheit = temperature * 33.8

print(fahrenheit)