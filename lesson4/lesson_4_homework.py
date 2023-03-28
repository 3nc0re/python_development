# Task 1
#
# The Guessing Game.
#
# Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated. The result should be sent back to the user via a print statement.

import random

rand_number = random.randint(1, 11)

number = int(input('Я загадав число від 1 до 10, спробуй вгадати: '))

if number == rand_number:
    print('Правильно!')
elif number != rand_number:
    print('Неправильно, правильне число: ' + str(rand_number))
else:
    print('Потрібно ввести номер')


# Task 2
#
# The birthday greeting program.
#
# Write a program that takes your name as input, and then your age as input and greets you with the following:
#
# “Hello <name>, on your next birthday you’ll be <age+1> years”

name = input('Write your name: ').title()
age = int(input('Write your age: '))
future_age = age + 1
print('Hello, ' + name +', on your next birthday you’ll be ' + str(future_age) + ' years')



# Task 3
#
# Words combination
#
# Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.
#
# For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters
#
# 'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …
# Tips: Use random module to get random char from string)

import random

input_string = input("Enter a word: ")

for i in range(5):
    random_string = ''.join(random.sample(input_string, len(input_string)))
    print(random_string)



