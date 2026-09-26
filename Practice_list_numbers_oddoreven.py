




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



