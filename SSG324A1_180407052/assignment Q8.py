'''
Create a dictionary for birthdays with a name as the key and a person’s birthday as the
value i.e birthdays = {“Anita”: “April 22”, “Hansel”: “August 3”}
● Ask the user for input of name
● print out the name of a person whose birthday is stored in the database
● if the person’s name is not in the database you should print “I do not have
birthday information for [name]”
● If the name is in the dictionary you should print “[Birthday] is the
birthday of [name]”

'''
birthdays = {"Anita": "April 22", "Hansel": "August 3", "Jodevo": "December 25", "Dele":"March 25"}
name = input('Please input your name: ')
if userInput in birthdays:

else:
    print("I do not have birthday information for [name]")

