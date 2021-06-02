def triangulo():

    lado1 = int(input("Ingrese el lado 1: "))
    lado2 = int(input("Ingrese el lado 2: "))
    lado3 = int(input("Ingrese el lado 3: "))    

    if (lado1 < (lado2+lado3)):
        print("Es un triángulo")
    elif (lado2< (lado1+lado3)):
        print("Es un triángulo")
    elif (lado3 < (lado1+lado2)):
        print("Es un triángulo")

    if((lado1 == lado2) and (lado1 == lado3) and (lado2==lado3)):
        print("Es un triángulo equilátero")

if __name__ == '__main__':
    triangulo()