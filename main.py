from Functions_basic_level import *
from Functions_mid_level import *
from Functions_adv_level import *
from general_functions import *
import os
valid = True
while valid:
    try:
        show_menu([
            "1. Basic",
            "2. Middle",
            "3. Advanced",
            "4. Exit"
        ], "Python Excercises")
        choice = input(MAGENTA + "What do you want to do? " + RESET)
        clear_screen()
        match choice:
            case "1":
                show_menu([
                    "1. Greeting",
                    "2. Add 2 numbers",
                    "3. Ever or Odd",
                    "4. Adult",
                    "5. Temperature",
                    "6. Area of a triangle",
                    "7. Larger in a list",
                    "8. Letter counter"
                ], "Basic Level")
                choice = input(MAGENTA + "What do you want to do? " + RESET)
                match choice:
                    case "1":
                        print(greeting("What is your name? "))
                    case "2":
                        num1 = int(input("Enter number 1: "))
                        num2 = int(input("Enter number 2: "))
                        print(f"{num1} + {num2} = {addNumbers(num1, num2)}")
                    case "3":
                        print(ever_or_odd(25))
                    case "4":
                        print(adult("What is your age? "))
                    case "5":
                        print(temperature("Enter the temperature in Celcius: "))
                    case "6":
                        print(triangleArea(2,4))
                    case "7":
                        print(larger_in_list())
                    case "8":
                        print(countLetter("Hello!", "l"))
            case "2":
                show_menu([
                    "1. Filter pairs",
                    "2. Palindrome",
                    "3. Factorial",
                    "4. Delete duplicate",
                    "5. FizzBuzz",
                    "6. Vowel counter",
                    "7. Text reverse"
                ], "Middle level")
                choice = input(MAGENTA + "What do you want to do? " + RESET)
                match choice:
                    case "1":
                        pairList()
                    case "2":
                        IsPalindrome()
                    case "3":
                        print(fact(5))
                    case "4":
                        print(delRepeated([1, 1, 2, 2, 3, 3]))
                    case "5":
                        FIZZBUZZ(5)
                    case "6":
                        word = input("Enter a word: ")
                        print(contVowel(word))
                    case "7":
                        word = input("Enter a word: ")
                        print(invert(word))
            case "3":
                    show_menu([
                    "1. Validate password",
                    "2. Dice simulator",
                    "3. Adding unique elemnts",
                    "4. Password generator",
                    "5. Functions composition",
                ], "Advanced level")
                    choice = input(MAGENTA + "What do you want to do? " + RESET)
                    match choice:
                        case "1":
                            password = input("Enter your password: ")
                            print("Welcome") if securePass(password) else print("The password does not match the requirements")
                        case "2":
                            print(diceSimulator())
                        case "3":
                            print(f"The sum of the unique numbers is: {addUnique([1, 1, 2, 2, 3, 3])}")
                        case "4":
                            lenPassword = int(input("How long do you want your password? "))
                            print(f"Your password is: {passGenerator(lenPassword)}")
            case "4":
                print(YELLOW + "Goodbye!" + RESET)
                valid = False
            case _:
                print(RED + "Invalid option! Please choose a valid option." + RESET)
    except ValueError:
        print(RED + "Invalid input, please enter a valid number." + RESET)
    except KeyboardInterrupt:
        print(YELLOW + "\nProgram interrupted by user." + RESET)
        break
