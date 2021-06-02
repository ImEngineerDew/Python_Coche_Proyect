def promedio():
    entrada1 = float(input("Ingrese la primera nota: "))
    entrada2 = float(input("Ingrese la segunda nota: "))
    entrada3 = float(input("Ingrese la tercera nota: "))

    promedio = (entrada1+entrada2+entrada3)/3

    if promedio <3.0:
        print("El promedio de notas es igual a: "+str(promedio))
        print("Ha suspendido el curso!")
    else:
        print("El promedio de notas es igual a: "+str(promedio))
        print("Aprobó el curso")    

if __name__ == '__main__':
    promedio()