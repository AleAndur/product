#Program number 1:  Write a Python program that ask a user to enter theirfavourite colour. If they
#                       enter“red”,“RED”or “Red”display the message“I like red too”. Otherwise display“I don’t
#                       like [colour], I prefer red”.

color = input(f"What is your favorite color: ")
if color == 'red' or color == 'Red' or color == 'RED':
      print('I like red too.')
else:
     print(f'I don’t like {color}, I prefer red.')

