'''
Write a program to accept a number from 1 to 7 and display the name of the day like 1
for Sunday , 2 for Monday and so on.

'''
userInput = int(input("Please kindly input a desired number between 1-7 : "))
if userInput == 1:
    print('Sunday')
elif userInput == 2:
    print('Monday')
elif userInput == 3:
    print('Tuesday')
elif userInput == 4:
    print('Wednesday')
elif userInput == 5:
    print('Thursday')
elif userInput == 6:
    print('Friday')
elif userInput == 7:
    print('Saturday')
else:
    print("Invalid input")