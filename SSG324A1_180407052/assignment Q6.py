'''
Write a program to accept percentage from the user and display the grade according to
the following criteria:
Marks Grade
> 90 A
> 80 and <= 90 B
>= 60 and <= 80 C
below 60 

'''
grade = input('kindly input your desired percentage to get the commensurate grade: ')
if grade > 90:
    print("Your gade is 'A'")
    