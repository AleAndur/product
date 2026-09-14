#5 Given the string:
#     word = "PYTHON"
#     Write a loop that prints each letter except H using Python “continue” statement.

word = 'PYTHON'
for letter in word:
    if letter == 'H':
        continue
    print(letter)

