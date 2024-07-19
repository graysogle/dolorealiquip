def my_generator():
    yield 4
    yield 2
    yield 0.0027010415357546814

# Create an iterator object from the generator function
my_iterator = my_generator()

# Iterate over the values using a loop
for value in my_iterator:
    print(value)
