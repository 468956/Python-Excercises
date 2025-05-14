from Functions_basic_level import *
from Functions_mid_level import *
from Functions_adv_level import *
from general_functions import *
import os
valid = True
while valid:
    try:
        show_menu()
        choice = input(MAGENTA + "What do you want to do? " + RESET)
        clear_screen()
        match choice:
            case "1":
                show_basic_menu()
                choice = input(MAGENTA + "What do you want to do? " + RESET)
                match choice:
                    case "1":
                        print(greeting("What is yout name?"))
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
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