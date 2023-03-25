# Task 1
#
# The greatest number
#
# Write a Python program to get the largest number from a list of random numbers with the length of 10
#
# Constraints: use only while loop and random module to generate numbers

import random

list_of_numbers = []
i = 0
while i < 10:
    list_of_numbers.append(random.randint(1, 20))
    i += 1
print(list_of_numbers)

largest_number = list_of_numbers[0]
i = 1
while i < 10:
    if list_of_numbers[i] > largest_number:
        largest_number = list_of_numbers[i]
    i += 1
print(largest_number)



# Task 2
#
# Exclusive common numbers.
#
# Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common integers between the 2 initial lists without any duplicates.
#
# Constraints: use only while loop and random module to generate numbers


list_1 = []
list_2 = []
i = 0
while i < 10:
    list_1.append(random.randint(1, 10))
    list_2.append(random.randint(1, 10))
    i += 1

list_3 = []
i = 0
while i < 10:
    if list_1[i] in list_2 and list_1[i] not in list_3:
        list_3.append(list_1[i])
    i += 1

print(list_1)
print(list_2)
print(list_3)


# Task 3
#
# Extracting numbers.
#
# Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.
#
# Constraint: use only while loop for iteration

numbers = list(range(1, 101))
final_list = []
i = 0
for i in numbers:
    if i % 7 == 0 and i % 5 !=0:
        final_list.append(i)
    i += 1
print(final_list)

