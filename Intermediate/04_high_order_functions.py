"""High order functions"""
from functools import reduce


def sum_one(value):
    return value + 1


def sum_five(value):
    return value + 5


def sum_two_values_and_add_one(first_value, second_value, f_sum_one):
    return f_sum_one(first_value + second_value)


print(sum_two_values_and_add_one(5, 2, sum_one))
print(sum_two_values_and_add_one(5, 2, sum_five))

"""Closures"""


def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value

    return add


print(sum_ten(3)(10))
add_closure = sum_ten(1)
print(add_closure(10))

"""Built-In High order functions"""

numbers = [2, 5, 10, 21, 3, 30]

# Map


def multiply_by_two(number):
    return number * 2


print(list(map(lambda number: number * 2, numbers)))

# Filter


def filter_greater_ten(number):
    if number > 10:
        return True
    else:
        return False


print(list(filter(filter_greater_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

#Reduce


def sum_two_values(value1, value2):
    return value1 + value2


print(reduce(sum_two_values, numbers))
