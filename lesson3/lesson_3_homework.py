 # Lesson 3 Homework
# Task 1
#
# String manipulation
#
# Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string.
#
# Sample String: 'helloworld'
#
# Expected Result : 'held'
#
# Sample String: 'my'
#
# Expected Result : 'mymy'
#
# Sample String: 'x'
#
# Expected Result: Empty String
#
# Tips:
#
# Use built-in function len() on an input string
# Use positive indexing to get the first characters of a string and negative indexing to get the last characters

string = input('Введіть слово: ')

if len(string) < 2:
    print('')
else:
    print(string[:2] + string[-2:])




# Task 2
#
# The valid phone number program.
#
# Make a program that checks if a string is in the right format for a phone number. The program should check that the string contains only numerical characters and is only 10 characters long. Print a suitable message depending on the outcome of the string evaluation.

input_number = input('Please, write a phone number: ')

if not input_number.isdigit():
    print('That is not a phone number!')
elif len(input_number) != 10:
    print('There must be 10 symbols)')
else:
    print('We will call you soon!')

# Task 3
#
# The math quiz program.
#
# Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong, and then responds with a message accordingly.

answer = input('Let`s play a quiz. How much is 234*46? ')

if not answer.isdigit():
    print('Only numbers please')
elif answer != 10764:
    print('Not correct answer')
else:
    print('Greetings! It`s correct answer')


# Task 4
#
# The name check.
#
# Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input. The program should check if your input is equal to the stored name even if the given name has another case, e.g., if your input is “Anton” and the stored name is “anton”, it should return True.

name = 'oleh'
name1 = input('Please write your name: ')

if name1.lower() == name:
    print(True)
else:
    print(False)