# Task 1
#
# Write a function called oops that explicitly raises an IndexError exception when called. Then write another function that calls oops inside a try/except state­ment to catch the error. What happens if you change oops to raise KeyError instead of IndexError?

def oops():
    raise KeyError("Oops! Key not found.")

def callable_oops():
    try:
        oops()
    except IndexError as i:
        print("Caught an IndexError:", i)
    except Exception as e:
        print("Caught some other error:", e)

callable_oops()



# Task 2
#
# Write a function that takes in two numbers from the user via input(), call the numbers a and b, and then returns the value of squared a divided by b, construct a try-except block which raises an exception if the two values given by the input function were not numbers, and if value b was zero (cannot divide by zero).

def square_divide():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        result = a ** 2 / b
        return result
    except ValueError:
        print("Error: Input values must be numbers.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

print(square_divide())
