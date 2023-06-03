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


"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():


