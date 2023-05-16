# Task 1
#
# Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and the number of occurrences as values.

sentence = input('Please write some sentence: ')

words_in_sentence = sentence.split()
words = {}

for i in words_in_sentence:
    if i in words:
        words[i] += 1
    else:
        words[i] = 1

print(words)



# Task 2
#
# Input data:
#
# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15
# }
# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }
#
# Compute the total price of the stock where the total price is the sum of the price of an item multiplied by the quantity of this exact item.

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_price = 0

for i in stock:
    if i in prices:
        total_price += stock[i] * prices[i]

print('Total price is: $' + str(total_price))



# Task 3
#
# List comprehension exercise
#
# Use a list comprehension to make a list containing tuples (i, j) where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.

list_comp = [(i, i ** 2) for i in range(1, 11)]
print(list_comp)
