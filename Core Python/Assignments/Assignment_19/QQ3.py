#Write a generator function that mimics the behavior of the built-in
# range() function. The generator should take start, stop, and step
# arguments and yield numbers within the specified range.

def my_range(start, stop=None, step=1):
    # Handle case where only one argument is provided
    if stop is None:
        stop = start
        start = 0

    if step == 0:
        raise ValueError("step argument must not be zero")

    if step > 0:
        while start < stop:
            yield start
            start += step
    else:
        while start > stop:
            yield start
            start += step

for i in my_range(5):
    print(i, end=" ")
