# Task #1

from module import greeting

def main():
    name = input('What is your name? ')
    greeting(name)

if __name__ == "__main__":
    main()


# Task 3
def mymod():
    def count_lines(name):
        with open(name, 'r') as file:
            return len(file.readlines())

    def count_chars(name):
        with open(name, 'r') as file:
            return len(file.read())

    def test(name):
        lines = count_lines(name)
        chars = count_chars(name)
        print("Lines:", lines)
        print("Chars:", chars)
