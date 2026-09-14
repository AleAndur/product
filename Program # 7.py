#7. Write a Python program to ask the user which direction the user wants to count (up
#     or down). If they select up, then ask them for the top number and then count from 1 to that
#     number. If they select down, ask them to enter a number below 20 and then count down from
#     20 to that number. If they enter something other than up or down, display the message “I don’t
#     understand”

up_or_down = input("Do you want to count up or down?: ...")
if up_or_down.lower() == "up":
   upwards = int(input("Up to which number do you want to count ..."))
   for counting in range(1, upwards + 1, 1):
      print(counting)

elif up_or_down.lower() == "down":
   downwards = int(input("Enter a number below 20 to countdown: ..."))
   for countdown in range(20, downwards -1, -1):
      print(countdown)

else:
   print("I don't undertand")