# Function with *args
# Problem:
# Write a function that takes variable number of arguments
# and returns their sum.


def sum_all(*args):
    print(args)
    """
    Calculates the sum of all the arguments passed.

    Args:
        *args: Variable number of arguments.

    Returns:
        int: The sum of all the arguments.

    Example:
        >>> sum_all(1, 2, 3)
        6
        >>> sum_all(10, 20, 30, 40)
        100
    """
    return sum(args)


print(sum_all(1, 2))
print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4))
print(sum_all(1, 2, 3, 4, 5))
print(sum_all(1, 2, 3, 4, 5, 6))
