"""List Comprehension"""

my_original_list = [1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

my_list = [i for i in range(8)]
print(my_list)

my_range = range(8)
print(list(my_range))

my_other_list = [i * i for i in range(8)]
print(my_other_list)
