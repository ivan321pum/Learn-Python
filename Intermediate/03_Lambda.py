"""Lambdas"""

sum_two_values = lambda num1, num2: print(num1 + num2)
print(sum_two_values(2, 4))

multiply_values = lambda first_value, second_value: first_value * second_value -3
print(multiply_values(5, 4))

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value


print(sum_three_values(5)(3, 5))
