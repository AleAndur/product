#Program number 2: Write a Python program to display a menu option. Then it will ask you to type a number
#                       between 1 and 4. If 1, 2, 3 and 4 are typed, the program displays "Added", "Searched",
#                       "Updated" and "Deleted" messages respectively. If any number is typed except 1 to 4, it
#                       quits with “Goodbye” message. The menu option looks like:
#                             1. Add
#                             2. Search
#                             3. Update
#                             4. Delete

menu = input(" 1. Add \n 2. Search \n 3. Update \n 4. Delete \n Please select an option:...")
if menu == '1':
      print("Added")
elif menu == '2':
      print('Searched')
elif menu == '3':
      print('Updated')
elif menu == '4':
      print('Deleted')
else:
      print("Goodbye")
