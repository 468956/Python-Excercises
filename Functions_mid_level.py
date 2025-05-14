# 🟡 Middle level

#     Filtrar pares
#     Crea una función que reciba una lista de números y devuelva solo los pares.
def pairList(numList):
    newlist = []
    for i in numList:
        if i % 2 == 0:
            newlist.append(i)
    return newlist

#print(pairList([1,2,3,4,5,6,7,8,9,10])) 
#     Palíndromo
#     Escribe una función que determine si un texto es un palíndromo.

def IsPalindrome():
        word = input("Enter a word: ").lower()
        Ispal = False
        for i in word:
            for j in word[::-1]:
                if i == j:
                    Ispal = True
                else:
                    Ispal = False
        if (Ispal == True):
            print("It is a palindrome.")
        else:
            print("It is not a palindrome.")

#     Factorial
#     Crea una función que calcule el factorial de un número entero positivo.

def fact(num):
    fact = 1
    for i in range(1,num+1):
        fact*=i
    return f"{num}! = {fact}"

#     Eliminar duplicados
#     Escribe una función que reciba una lista y devuelva una nueva sin elementos repetidos.

def delRepeated(elemList):
    seen = []
    newElemList = []
    for i in elemList:
        if i in seen:
            newElemList.append(i)
        else:
            seen.append(i) 
    return seen
#     FizzBuzz
#     Crea una función que reciba un número y devuelva "Fizz", "Buzz" o "FizzBuzz" según las reglas del juego.

def FIZZBUZZ(number):
    if (number % 3 == 0 and number % 5 == 0):
            print(f"Number: {number}. FizzBuzz")
    elif (number % 3 == 0):
            print(f"Number: {number}. Fizz")
    elif (number % 5 == 0):
            print(f"Number: {number}. Buzz")
    else:
            print(f"The number {number} is not fizz, buzz or fizzbuzz")


#     Contar vocales
#     Escribe una función que reciba una cadena y devuelva la cantidad de vocales.

def contVowel(word):
    contVowel = 0
    for i in word.lower():
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "o":
            contVowel += 1
    return f"There are {contVowel} vowel" if contVowel == 1 else f"There are {contVowel} vowels"
             
#     Invertir texto
#     Crea una función que invierta una cadena de texto.
def invert(word):
    rever = ""
    for i in word:
         rever = i + rever
    return rever  
#invert("")
