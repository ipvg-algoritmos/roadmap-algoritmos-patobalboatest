# Juego de cachipun
import random


contador_j = 0
contador_m = 0
respuesta = "si"

while respuesta=="si" or (ju)

    print(f"PUNTAJE = Jugador: {contador_j}     CPU: {contador_m}")
    eleccion = input("Ingresa papel, piedra o tijera: ").lower()
    tipos_de_mano = ["piedra","papel","tijera", "diosito"]
    maquina = random.choice(tipos_de_mano)
    print(f"{eleccion} vs {maquina}") 

    
    if eleccion == maquina:
        print("Esto es un Empate")
    elif maquina == "diosito":
        print("Ganó diosito")
    elif (eleccion == "tijera" and maquina == "papel") or \
        (eleccion == "piedra" and maquina == "tijera") or \
        (eleccion == "papel" and maquina == "piedra"):
        print("Ganaste")
        contador_j = contador_j + 1
    else:
        print("Perdiste")
        contador_m = contador_m + 1
    respuesta = input("Deseas seguir jugando (si/no)")
