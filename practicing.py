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