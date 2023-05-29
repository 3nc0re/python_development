class MyIterable:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        return iter(self.iterable)

    def __getitem__(self, index):
        return self.iterable[index]

my_list = [1, 2, 3, 4, 5]
my_iterable = MyIterable(my_list)


for item in my_iterable:
    print(item)

print(my_iterable[2])  # Output must be: 3
print(my_iterable[3])  # Output must be: 4
print(my_iterable[-1])  # Output must be: 5
