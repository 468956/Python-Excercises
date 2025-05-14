CYAN = "\033[96m"
GREEN = "\033[92m"
MAGENTA = "\033[95m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# 🟢 Nivel Básico

    # Saludo personalizado
    # Crea una función que reciba un nombre y muestre un saludo personalizado.
# ANSI color codes
def show_basic_menu():
    options = [
            "1. Greeting",
            "2. Add 2 numbers",
            "3. Ever or Odd",
            "4. Adult",
            "5. Temperat    ure",
            "6. Area of a triangle",
            "7. Exit"
        ]

    title = "MAIN MENU"

    max_width = max(len(option) for option in options)
    total_width = max(len(title), max_width) + 6

    print(CYAN + "╔" + "═" * total_width + "╗" + RESET)
    print(CYAN + "║" + RESET + title.center(total_width) + CYAN + "║" + RESET)
    print(CYAN + "╠" + "═" * total_width + "╣" + RESET)

    for option in options:
        print(CYAN + "║" + RESET + "  " + GREEN + option.ljust(total_width - 2) + RESET + CYAN + "║" + RESET)

    print(CYAN + "╚" + "═" * total_width + "╝" + RESET)

def greeting(message):
    name = input(message)
    return GREEN + f"Hello, {name}!" + RESET

    # Suma de dos números
    # Escribe una función que reciba dos números y devuelva su suma.

def addNumbers(num1, num2):
    return int(num1+num2)

    # Número par o impar
    # Crea una función que determine si un número es par o impar.

def ever_or_odd(num):
    if num % 2 == 0:
        return f"{GREEN} Number {num} is even."
    else:
        return  f"{GREEN} Number {num} is not even."

    # Mayoría de edad
    # Escribe una función que reciba una edad y devuelva si es mayor o menor de edad.

def adult(message):
    age = input(message)
    return f"{GREEN} You are an adult.{RESET}" if age >= "18" else f"{RED} You are not an adult.{RESET}"
#print(adult("Enter your age: "))

    # Conversor de temperatura
    # Crea una función que convierta grados Celsius a Fahrenheit.

def temperature(message):
    temp = int(input(message))
    return (f"{GREEN}{temp}°C = {temp*(9/5)+32}°F{RESET}")

    # Área de un triángulo
    # Escribe una función que devuelva el área de un triángulo dado su base y altura.
def triangleArea(b,h):
    return f"{GREEN}{0.5*int(b)*int(h)}{RESET}"
#print(triangleArea(2, 4))

    # Mayor de una lista
    # Crea una función que reciba una lista de números y devuelva el mayor.
def larger_in_list(numList):
    for i in numList:
        if i > i:
            larger = i
    return f"The larger number is: {i}"

    # Contar letras
    # Escribe una función que cuente cuántas veces aparece una letra en una palabra.
def countLetter(word, letter):
    cont = 0
    if not letter in word:
        return f"{letter} is not in {word}"
    for i in word:
        if i == letter:
            cont += 1
    return f"{letter} appears {cont} time" if cont == 1 else f"{letter} appears {cont} times"
