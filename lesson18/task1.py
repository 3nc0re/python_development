
def with_index(iterable, start=0):
    index = start
    for item in iterable:
        yield index, item
        index += 1

my_list = ['car', 'truck', 'bicycle']

for index, item in with_index(my_list, start=1):
    print(index, item)
