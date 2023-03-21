# Task 1
#
# The greeting program.
#
# Make a program that has your name and the current day of the week stored as separate variables and then prints a message like this:
#
#      "Good day <name>! <day> is a perfect day to learn some python."
# Note that  <name> and <day> are predefined variables in source code.
#
# An additional bonus will be to use different string formatting methods for constructing result string.

name = 'Oleh'
day = 'Sunday'
print('Good day '+ name + '!' + ' ' + day + ' is a perfect day to learn some python.')

# Task 2
#
# Manipulate strings.
#
# Save your first and last name as separate variables, then use string concatenation to add them together with a white space in between and print a greeting.

first_name = 'Oleh '
last_name = 'Mykhailiak'
print(first_name + last_name)

# Task 3
#
# Using python as a calculator.
#
# Make a program with 2 numbers saved in separate variables a and b, then print the result for each of the following:
#
# Addition
# Subtraction
# Division
# Multiplication
# Exponent (Power)
# Modulus
# Floor division

num1 = 4
num2 = 7
print('Addition is ' + str(num1 + num2))
print('Subtraction is ' + str(num1 - num2))
print('Division is ' + str(num1 / num2))
print('Multiplication is ' + str(num1 * num2))
print('Exponent (Power) is ' + str(num1 ** num2))
print('Modulus is ' + str(num1 % num2))
print('Floor division is ' + str(num1 // num2))

