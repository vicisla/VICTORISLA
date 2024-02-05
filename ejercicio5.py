#Juego adivinar el numero
import random
randomNum = random.randint(1,25)
intentos=0
print("Intenta divinar el numero, tienes 10 intentos")

#Creando funcion para contar numero de intentos realizados.

while intentos<10:
    print(f"tienes: {intentos}")
    intentos=int(input())
    intentos+=1
    if intentos<randomNum:
        print("Numero bajo")
    elif intentos>randomNum:
        print("Numero bajo")
    else:
        break
if intentos==randomNum:
    print(f"Adivinaste el numero")
else:
    print(f"Perdites, el numero era: {randomNum}")   
