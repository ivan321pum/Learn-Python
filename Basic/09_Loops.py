"""Loops"""

# While
my_condition = 1

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else:  # hay else!!!!. Recuerda que no se puede poner un elif en un while
    print("Mi condición es mayor o igual que 10")

print("La ejecución continua")

while my_condition < 20:
    if my_condition != 15:  # condicionales dentro del bucle
        print(my_condition)
        my_condition += 1
    else:
        print("El numero es 15, el numero 15 es muy feo, por lo tanto procederé a detener la ejecución")
        break  # a diferencia de exit() esto no para el programa, simplemente rompe el bucle
else:
    print("El numero es mayor o igual que 20")
print("La ejecución continua")
# for

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")

for element in my_tuple:
    print(element)

my_other_set = {"Iván", "Sevilla", 15}

for element in my_other_set:
    print(element)

my_other_dict = {"Nombre": "Iván", "Apellido": "Sevilla", "Edad": "15", 2: "Se pueden números!"}

for element in my_other_dict.values():  # element no es una palabra reservada, es una variable que podemos ponerle el nombre que queramos
    print(element)  # en los for sí que se pueden else pero no elif
    if element == "Edad":
        continue  # mejor no utilizar el continue
    print("se ejecuta")
else:
    print("El bucle ha finalizado")
