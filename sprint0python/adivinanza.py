from random import sample

npreguntas = 0
preguntas = [1, 2, 3]

puntuacion = 0

while npreguntas < 2:
    pregunta = sample(preguntas, k=1)[0]

    if pregunta == 1:
        print("¿De qué color es el caballo blanco de Santiago?")
        print("a. Negro")
        print("b. Marrón")
        print("c. Blanco")

        respuesta = input("Elige entre a/b/c: ")

        if respuesta == "c":
            print("Respuesta correcta, que grande, toma 10 puntos")
            puntuacion += 10
        else:
            print("Respuesta incorrecta, -5 puntos")
            puntuacion -= 5

    elif pregunta == 2:
        print("¿Cuantos animales de cada especie llevó Noé en su Arca?")
        print("a. 2")
        print("b. 1")
        print("c. Ninguna de las anteriores")

        respuesta = input("Elige entre a/b/c: ")

        if respuesta == "c":
            print("Respuesta correcta, ¿fue suerte o sabías que era Noé y no Moisés? +10 puntos")
            puntuacion += 10
        else:
            print("Respuesta incorrecta, -5 puntos")
            puntuacion -= 5

    elif pregunta == 3:
        print("Si te pudieras ver reflejado/a en un espejo que está a 10 años luz, ¿qué verías?")
        print("a. A tu Yo de dentro de 10 años")
        print("b. A tu Yo de hace 10 años")
        print("c. A tu Yo actual")

        respuesta = input("Elige entre a/b/c: ")

        if respuesta == "b":
            print("Veo que eres algún tipo de genio, +10 puntos")
            puntuacion += 10
        else:
            print("Respuesta incorrecta, -5 puntos")
            puntuacion -= 5
            explicacion = input("¿Quieres conocer la explicación? (s/n): ")

            if explicacion == "s":
                print("Pues esto se debe a que la luz que emite tu cuerpo tardaría 10 años en llegar hasta el espejo, pero tú tienes que estar viendo algo reflejado, ya que no puede ser que no estés viendo nada, por lo que verías reflejada la luz que acaba de llegar, es decir, la que se emitió hace 10 años, por ende, la imagen de tu Yo del pasado.")

    npreguntas += 1
    print()

    preguntas.remove(pregunta)

print()

if puntuacion >= 0:
    print("No está mal para una primera vez: " + str(puntuacion) + " puntos")
else:
    print("Ni siquiera lo has intentado, ¿verdad?: " + str(puntuacion) + " puntos")

