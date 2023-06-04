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
 * Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
 */"""


def dont_repeat_numbers(str1, str2):
    str1 = str1.lower()
    str1_list = [char for char in str1]
    str2 = str2.lower()
    str2_list = [char for char in str2]

    non_repeated_chars_str1 = []
    non_repeated_chars_str2 = []

    for char in str1_list:
        if char not in str2_list:
            non_repeated_chars_str1.append(char)

    for char in str2_list:
        if char not in str1_list:
            non_repeated_chars_str2.append(char)

    out1 = "".join(non_repeated_chars_str1)
    out2 = "".join(non_repeated_chars_str2)
    return out1, out2


print(dont_repeat_numbers("sube", "baja"))


"""/*
 * Escribe una función que calcule y retorne el factorial de un número dado
 */"""


def recursive(num):
    output = 1
    while num != 1:
        output = output * num
        num -= 1
    return output


print(recursive(4))

"""/*
 * Escribe una función que calcule si un número dado es un número de Armstrong
 * (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información 
 * al respecto.
 */"""


def transform_int_into_list(num):
    strings = str(num)
    digits = []
    for char in strings:
        digits.append(int(char))
    return digits


def transform_list_into_int(the_list):
    the_int = sum(the_list)
    return the_int


def armstrong_number(num):
    digits = transform_int_into_list(num)
    number_of_digits = len(digits)
    elevated_number = 0
    sum_of_powers = 0
    for digit in digits:
        sum_of_powers += digit ** number_of_digits
    if sum_of_powers == num:
        return True
    else:
        return False


print(armstrong_number(8207))

"""/*
 * Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */"""


def capitalize_first_letter(string):
    words = string.split()  # Dividir la cadena en palabras separadas
    capitalized_words = []
    for word in words:
        capitalized_word = word[0].upper() + word[1:]  # Convertir la primera letra en mayúscula
        capitalized_words.append(capitalized_word)
    capitalized_string = " ".join(capitalized_words)  # Unir las palabras con espacios
    return capitalized_string


print(capitalize_first_letter("don't stop me now"))
