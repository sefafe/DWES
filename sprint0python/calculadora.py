from operaciones import suma, resta, multiplicacion, division

repetir="s"
while(repetir=="s"):
    num1=int(input("Ingresa el primer número: "))
    num2=int(input("Ingresa el segundo número: "))
    print()
    print("¿Qué deseas hacer?")
    print("a. Sumar")
    print("b. Restar")
    print("c. Multiplicar")
    print("d. Dividir")
    print()
    respuesta=input("Elige entre a/b/c/d: ")
    print()
    if respuesta=="a":
        suma(num1,num2)
    elif respuesta=="b":
        resta(num1,num2)
    elif respuesta=="c":
        multiplicacion(num1,num2)
    elif respuesta=="d":
        division(num1,num2)
    print()
    repetir=input("¿Realizar otra operación? (s/n): ")
    while repetir!="s" and repetir!="n":
        repetir=input("¿Realizar otra operación? (s/n): ")

    