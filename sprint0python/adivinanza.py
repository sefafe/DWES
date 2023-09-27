print("¿De qué color es el caballo blanco de Santiago?")
print("a. Negro")
print("b. Marrón")
print("c. Blanco")
puntuacion=0
respuesta= input("Elige entre a/b/c: ")
if respuesta=="a":
    print("Respuesta incorrecta, -5 puntos")
    puntuacion=puntuacion-5 
elif respuesta=="b":
    print("Respuesta incorrecta, -5 puntos")
    puntuacion=puntuacion-5 
elif respuesta=="c":
    print("Respuesta correcta, que grande, toma 10 puntos")
    puntuacion=puntuacion+10 
else:
    print("Esa ni siquiera era una opción, -5 puntos por espabilado/a")
    puntuacion=puntuacion-5 
print()

print("¿Cuantos animales de cada especie llevó Moisés en su Arca?")
print("a. 2")
print("b. 1")
print("c. Ninguna de las anteriores")
respuesta= input("Elige entre a/b/c: ")
if respuesta=="a":
    print("Habrías acertado... si supieras leer, -5 puntos")
    puntuacion=puntuacion-5 
elif respuesta=="b":
    print("Respuesta incorrecta, -5 puntos")
    puntuacion=puntuacion-5 
elif respuesta=="c":
    print("Respuesta correcta, ¿fue suerte o sabías que era Noé y no Moisés? +10 puntos")
    puntuacion=puntuacion+10 
else:
    print("Esa ni siquiera era una opción, -5 puntos por espabilado/a")
    puntuacion=puntuacion-5 
print()

print("Si te pudieras ver reflejado/a en un espejo que está a 10 años luz, ¿qué verías?")
print("a. A tu Yo de dentro de 10 años")
print("b. A tu Yo de hace 10 años")
print("c. A tu Yo actual")
respuesta= input("Elige entre a/b/c: ")
if respuesta=="a":
    print("La intención es lo que cuenta, pero -5 puntos igualmente")
    puntuacion=puntuacion-5 
elif respuesta=="b":
    print("Veo que eres algún tipo de genio, +10 puntos")
    puntuacion=puntuacion+10
elif respuesta=="c":
    print("Bueno, es una respuesta respetable, aunque no es correcta, -5 puntos")
    puntuacion=puntuacion-5
else:
    print("Esa ni siquiera era una opción, -5 puntos por espabilado/a")
    puntuacion=puntuacion-5
print()

explicacion=input("¿Quieres conocer la explicación? (s/n): ")
if explicacion=="s":
    print("Pues esto se debe a que la luz que emite tu cuerpo tardaría 10 años en llegar hasta el espejo, pero tú tienes que estar viendo algo reflejado, ya que no puede ser que no estés viendo nada, por lo que verías reflejada la luz que acaba de llegar, es decir, la que se emitió hace 10 años, por ende, la imagen de tu Yo del pasado.")

print()
if puntuacion>=0:
    print("No está mal para una primera vez "+str(puntuacion)+" puntos")
else:
    print("Ni siquiera lo has intentado, ¿verdad? "+str(puntuacion)+" puntos")
