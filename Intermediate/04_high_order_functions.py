"""High order functions"""


def sum_one(value):
    return value + 1


def sum_five(value):
    return value + 5


def sum_two_values_and_add_one(first_value, second_value, f_sum_one):
    return f_sum_one(first_value + second_value)


print(sum_two_values_and_add_one(5, 2, sum_one))
print(sum_two_values_and_add_one(5, 2, sum_five))

"""Closures"""


def sum_ten():
    def add(value):
        return value + 10
    return add


print(sum_ten()(10))
add_closure = sum_ten()
print(add_closure(10))
