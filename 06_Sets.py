### Sets ###

my_set = set()
my_other_set = {}
print(type(my_other_set))  # es un diccionario si lo ponemos de esta manera, ya que se defina de la misma forma
print(type(my_set))  # es un tipo de dato

my_other_set = {"Iván", "Sevilla", 15}
print(type(my_other_set))  # se transforma en set

print(len(my_other_set))

print(my_other_set)
# print(my_other_set[1]) esto va a dar error, no se puede

my_other_set.add("ivan321pum")
print(my_other_set)  # no es una estructura ordenada, se desordena al imprimir
my_other_set.add("ivan321pum")  # un set no admite repetidos, solo pone uno
print(my_other_set)

print("Iván" in my_other_set)  # puedes buscar un elemento si existe
print("Ixán" in my_other_set)

my_other_set.remove("Iván")  # se puede borrar
print(my_other_set)

my_other_set.clear()  # borra todo lo que hay
print(my_other_set)
print(len(my_other_set))

del my_other_set
# print(my_other_set) ya no existe

# recuerda que también se puede pasar a lista

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))
print(my_new_set.difference(my_set))
