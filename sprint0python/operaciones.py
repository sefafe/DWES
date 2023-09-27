num1=int(input("Ingresa el primer número: "))
num2=int(input("Ingresa el segundo número: "))
repetir="s"
while(repetir=="s"):
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
        num3=num1+num2
        print ("El resultado de la suma es: "+str(num3))
    elif respuesta=="b":
        num3=num1-num2
        print ("El resultado de la resta es: "+str(num3))
    elif respuesta=="c":
        num3=num1*num2
        print ("El resultado de la multiplicación es: "+str(num3))
    elif respuesta=="d":
        if num2==0:
            print("No se puede dividir entre 0")
        else:
            num3=num1/num2
            print ("El resultado de la división es: "+str(num3))
    print()
    repetir=input("¿Realizar otra operación? (s/n): ")

