"""Functions"""


def my_function():
    mis_mierdas = "Caca"
    if mis_mierdas == "Caca":
        print("Xd")


my_function()
my_function()
my_function()


def sum_two_values(value_1, value_2):
    if type(value_1) and type(value_2) == int:
        print(value_1 + value_2)
    else:
        print("Tonto, pon numeros")


sum_two_values(6, 4)


def sum_two_values_with_return(value_1, value_2):
    return value_1 + value_2


my_result = sum_two_values_with_return(3, 6)  # puedo guardarme lo que devuelve con return
print(my_result)


def print_name (name, surname):
    print(f"Mi nombre es {name} y mi apellido {surname}")


print_name(surname="Sevilla", name="Iván")


def print_name_with_default(name, surname, alias = "Sin alias"):  # esto hace que si no tiene nada por defecto es esto
    print(f"Mi nombre es {name}, mi apellido {surname} y mi alias es {alias}")


print_name_with_default("Iván", "Sevilla")


def print_texts(*texts):  # poniendo el arterisco se pueeden poner todos los parametros que quieras
    for text in texts:
        print(text)


print_texts("Hola", "Como", "Estas", "Estos", "Son", "Varios", "Parametros")
