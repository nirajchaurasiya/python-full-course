# Function with **kwargs
# Problem:
# Create a function that accepts any number of keyword arguments
# and prints


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="shaktiman", power="laser")
print_kwargs(name="shaktiman")
print_kwargs(name="shaktiman", power="laser", enemy="Dr. Jackaal")
