import random
# 🔴 Nivel Avanzado

#     Validar contraseña segura
#     Escribe una función que valide si una contraseña cumple con requisitos de seguridad (mayúsculas, minúsculas, números y símbolos).

def securePass(password):
    specialCar = ['!', '@', '#', '$', '%', '^', '&', '*']
    if not any(i.isupper() for i in password):
         return False
    if not any(i.islower() for i in password):
         return False
    if not any(i in password for i in specialCar):
         return False
    if not any(i.isdigit() for i in password):
         return False
    return True


#     Simular dado
#     Crea una función que simule el lanzamiento de un dado de 6 caras.
def diceSimulator():
    return f"Your number is: {random.randint(1, 6)}"

#     Suma de elementos únicos
#     Escribe una función que reciba una lista de números y devuelva la suma de los elementos únicos.
def addUnique(elemList):
     seen = []
     newElemList = []
     for i in elemList:
          if i in seen:
               newElemList.append(i)
          else:
               seen.append(i)
     return sum(seen)
#     Generador de contraseñas
#     Crea una función que genere una contraseña aleatoria de una longitud dada.
def passGenerator(lenPassword):
     newPassword = "" 
     for i in range(lenPassword):
          newPassword += random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*'])
     return newPassword
print(passGenerator(14))
#     Composición de funciones
#     Escribe una función que reciba otra función como parámetro y aplique una composición de funciones.
def addNumbers(num1, num2):
    return int(num1+num2)
    

