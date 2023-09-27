import random
print("Bienvenido al piedra, papel y tijera: ")
miPuntuacion=0
suPuntuacion=0
partidas=0

a="Piedra"
b="Papel"
c="Tijera"
while partidas<5:
    print("Partida número "+str(partidas+1)+" de 5")
    print()
    print("a. Piedra")
    print("b. Papel")
    print("c. Tijera")
    print()
    jugada=input("Elige una jugada: ")
    print()
    if jugada=="a":
        jugada=a
    elif jugada=="b":
        jugada=b
    elif jugada=="c":
        jugada=c

    posiblesJugadas=[a,b,c]
    jugadaRival=random.choice(posiblesJugadas)
    print("Has elegido "+jugada+" y el rival ha elegido... "+jugadaRival)

    if (jugada==a and jugadaRival==c) or (jugada==b and jugadaRival==a) or (jugada==c and jugadaRival==b):
        print("Has ganado el duelo")
        miPuntuacion=miPuntuacion+1
        partidas=partidas+1
    elif (jugada==c and jugadaRival==a) or (jugada==a and jugadaRival==b) or (jugada==b and jugadaRival==c):
        print("Mala suerte")
        suPuntuacion=suPuntuacion+1
        partidas=partidas+1
    else:
        print("Habeis empatado")
print()
print ("Tu puntuación: "+str(miPuntuacion))
print ("Puntuación de la máquina: "+str(suPuntuacion))



