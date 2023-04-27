# Condicionales #
my_condition = True
my_other_condition = "xd"

if my_condition == False:
    print("Es falso!!")


if my_other_condition != True or False:  # también se puede poner type(bool)
    print("Es true")

mi_number = 5

if mi_number >= 10:
    print("Es mayor o igual que 10")
else:
    print("Es menor que 10")

my_new_condition = 34

if my_new_condition > 24:
    print("Es mayor que 24")
elif my_new_condition > 34:  # else if
    print("Es mayor que 14")
