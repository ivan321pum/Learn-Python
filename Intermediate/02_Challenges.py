"""Challenges"""

"""
EL FAMOSO "FIZZ BUZZ”:
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

print("Fizzbuzz")
def fizzbuzz():
    for current_num in range(1, 101):
        if current_num % 3 == 0 and current_num % 5 == 0:
            print("fizzbuzz")
        elif current_num % 3 == 0:
            print("fizz")
        elif current_num % 5 == 0:
            print("buzz")
        else:
            print(current_num)

fizzbuzz()

print("anagrama")
"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""


def is_anagram(word1, word2):
    if word1.lower() == word2.lower():
        return False
    else:
        return sorted(word1.lower()) == sorted(word2.lower())


print(is_anagram("amor", "amor"))


print("Fibonacci")
"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""


def fibonacci():
    penultimo_numero = 0
    ultimo_numero = 1
    print(penultimo_numero)
    print(ultimo_numero)
    for index in range(0, 50):
        numero_actual = ultimo_numero + penultimo_numero
        print(numero_actual)
        penultimo_numero = ultimo_numero
        ultimo_numero = numero_actual


fibonacci()

"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
"""


def is_a_prime_number(number):
    if number >= 2:
        for index in range(2, number):
            if number % index == 0:
                return False
            else:
                return True
    else:
        return True


print(is_a_prime_number(1))

"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""


def inverter_3000(string):
    reversed_string = string[::-1]
    return reversed_string


print(inverter_3000("Hola mundo"))


"""/*
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */"""

