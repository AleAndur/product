




#1. Write a Python program to ask a user for number below 50 and then display from that number to 50. Make sure you show the number they entered in the output.

number = int(input('Give me a number under 50: ...'))
print("you have chosen: ", number)
for i in range(number, 51):
    print(i)

# 2. Write a Python program to ask the user to enter their name and display each letter in their name on a separate line.

name = input('Please tell me your name: ')
for i in name:
    print(i)


#3.Write a Python program that uses a loop to go through numbers from 1 to 10. For each number:
	#Print "Even" if the number is even
	#Print "Odd" if the number is odd

for i in range(1, 11):
    if i % 2 == 0:

        print(i,"Even")
    else:
        print(i, "Odd")

# FOR LOOPS:

# 4. Write a program using range() to print numbers from 1 to 10.

for i in range(1, 11):
    print(i)
#5. Use range() to print all even numbers between 2 and 20.
for i in range(2, 22, 2):
    print(i)
#6. Write a program using range() to print numbers from 20 down to 10.
for i in range(20, 9, -1):
    print(i)
#7. Use range() to print numbers from 1 to 20, counting by 3.
for i in range(1, 20, 3):
    print(i)
#8 Use a for loop to display the 5 times table from 1 to 10.
# Example Output:
# 5 x 1 = 5
# 5 x 2 = 10

for i in range(1,11):
    print(f"5 x {i} = {i * 5}")
#9 Write a Python program that repeatedly asks the user to enter numbers, stops when the user enters 0, and then displays the total sum of all the entered numbers

total = 0
total_sum = int(input("Enter number: "))
while total_sum != 0:
    total += total_sum
    total_sum = int(input("Enter number: "))
print("This is the total", total)

#10. Ask the user for a product name, price, and quantity. Calculate and print the total cost, formatted to 2 decimal places using an f-string.


name = input("Give me a product name: ")
price = float(input('Enter the price: '))
quantity = int(input('How many?: '))
calculation = price * quantity
print(f"Total cost: {calculation:.2f}")


#11. Write a program that stores your age as a string, then casts it to an int and prints type() before and after casting.

age_string = str(input("Give me your age: "))
print(f'Your age is a string: {type(age_string)}')
print(f'Your age is an integer: {type(int(age_string))}')
#12. Ask for a temperature in Celsius (as input) and convert it to Fahrenheit, printing both values with labels.

celsius_temperature = int(input('Give me the temperatura in Celsius: '))
fahrenheit = (celsius_temperature * 9 / 5) + 32
print(f'This is temperature in Celsius {celsius_temperature} and this your temperature in Fahrenheit {fahrenheit}')

#12. Take two numbers from the user and print the results of all 7 arithmetic operators (+, -, *, /, //, %, **) with labels.

one = float(input("Give me first number: "))
two = float(input('Give me the second number:'))
while two == 0:
    print(f"We cannot divide by zero, but here are the rest:\nAddition: {one + two}\nSubtraction: {one - two}\nMultiplication: {one * two}\nExponentiation: {one ** two}")
    break
else:
    print(f'Addition: {one + two}\nSubtraction: {one - two}\nMultiplication: {one * two}\nDivision: {one / two}\nFloor Division: {one // two}\nOnly the remainder: {one % two}\nExponentiation: {one ** two}')

#13. Ask for three exam scores and use comparison + logical operators to print True/False for: "all three are above 50", "at least one is above 90".
# comparison operator ==, >, < , !=, >=, <=.
# logical operators: AND, OR, NOT.

examScore_one = int(input('Score number one: '))
examScore_two = int(input('Score number two: '))
examScore_three = int(input('Score number three: '))
if examScore_one > 50 and examScore_two > 50 and examScore_three > 50:
    print('All three are above 50: ->', True)
else:
    print('Not all three are above 50',False)

if examScore_one > 90 or examScore_two > 90 or examScore_three > 90:
    print('At least one is above 90: ->', True)
else:
    print('None of them are above 90',False)
#14. Write a program using +=, -=, *= to simulate a bank balance that receives a deposit, a withdrawal, and interest.
bank_balance = 450
action = int(input('Type:\n1.Deposit\n2.Withdraw\n3.Interest:\n '))
amount = float(input('Amount: '))
if action == 1:
    bank_balance += amount
    print('You deposited: ', amount, 'Your new balance is: ',bank_balance)
elif action == 2:
    bank_balance-= amount
    print('You withdrew:', amount, 'Your new balance is : ',bank_balance)
elif action == 3:
    interest = amount / 100
    interest += 1
    print('This is the interest multiplier: ', interest)
    bank_balance *= interest
    print('Your new balance with interest is:', bank_balance)
else:
    print("Error: Wrong input.")

#Take a user's mark (0–100) and print a grade: A (70+), B (60–69), C (50–59), D (40–49), F (below 40) — use if/elif/else.

user_mark = int(input('Give me a mark between 0 and 100: '))
if user_mark < 40:
    print("F-grade")
elif user_mark > 40 or user_mark < 49:
    print('D-Grade')
elif user_mark > 50 or user_mark < 59:
    print('C-Grade')
elif user_mark > 60 or user_mark < 69:
    print('B-Grade')
else:
    print('A-Grade')


#A cinema charges: under 12 → £5, 12–17 → £8, 18–64 → £12, 65+ → £6. Ask for age and print the ticket price.
#Write a nested if program: check if a number is positive/negative/zero, and if positive, also check if it's odd or even.
#A gym membership gives a discount if (age is 18–21) OR (has a student ID = "yes"). Take both inputs and print the discount status using a compound Boolean expression.