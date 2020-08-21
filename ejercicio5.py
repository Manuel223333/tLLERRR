primernumero = int(input("Introduce primer número: "))
segundonumero = int(input("Introduce segundo número: "))

if primernumero > segundonumero:

    for contador in range(segundonumero, (primernumero + 1)):
        print(contador)

else:
    print("El segundonumero debe ser menor al primernumero")