# Dictionaries #

my_dict = {}  # asi se declara
my_other_dict = dict()  # asi también
print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Iván", "Apellido": "Sevilla", "Edad": "15", 2: "Se pueden números!"}
print(my_other_dict)
print(my_other_dict["Edad"])

my_dict = {
    "Nombre": "Iván",
    "Apellido": "Sevilla",
    "Edad": "15",
    2: "Se pueden números!",
    "Lenguajes": {"C#", "Python"}  # se puede cualquier otra cosa dentro de un diccionario, incluso otro diccionario
}
print(my_dict["Nombre"])
print(my_dict["Lenguajes"])
print(type(my_dict["Lenguajes"]))

print(len(my_other_dict))
print(len(my_dict))

my_dict["Calle"] = "Calle Primavero"  # se pueden agragar cosas
print(my_dict)

del my_dict["Calle"]  # asi se eliminan
print(my_dict)

print("Nombre" in my_dict)  # esto sí que esta
print("Iván" in my_dict)  # esto no está

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "MoureDev")
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))