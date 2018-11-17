import random

# Dificultades
#    Facil: Dejarlo asi como esta
#    Medio: Aumentar rango del 1 al 40
#    Dificil: Reducir numero de intentos a 3

# Recuerden actualizar la interfaz y desplegar los rangos adecuados
# Y pedir que introdusca la dificultad.

def jugar():

    contador=0
    intentos=0

    numero_aleatorio=random.randint(1,10)

    print("Bienvenido a Adivina el Número.")
    print("Estoy pensando en un número del 1 al 10.")
    print("Adivina cual es")
    print("Solo tienes 5 intentos.")

    while intentos < 5:

        try:
            adivinanza=int(input("El número es: "))
        except ValueError:
            print("Ese no es un número valido!!!")
        else:
            if adivinanza == numero_aleatorio:

                print("Adivinaste!!!")
                contador += 1
                print("Lo lograste en",contador,"jugadas.")

                jugar_nuevamente=input("Quieres jugar de nuevo? si/no ")

                if jugar_nuevamente.lower() == "si":
                    jugar()
                elif jugar_nuevamente.lower() == "no":

                    break

            elif numero_aleatorio > adivinanza:
                print("Fallaste, mi número es mayor...")

            else:
                print("Fallaste, mi número es menor")

            contador +=1

            intentos += 1
            print("Intento {}/5 ".format(intentos))

    else:
        print("Se te acabaron los intentos.")

        jugar_nuevamente=input("Quieres jugar de nuevo? si/no: ")

        if jugar_nuevamente.lower() == "si":
            jugar()


jugar()
print("Gracias por jugar.")
