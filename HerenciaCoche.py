class Coche:
    def __init__ (self, llantas, puerta, combustible,motor):
        self._llantas = llantas
        self._puerta = puerta
        self._combustible = combustible
        self._motor = motor
    
    @property
    def coche(self):
        return self._llantas
    def puerta (self):
        return self._puerta
    def combustible (self):
        return self._combustible
    def motor(self):
        return self._motor
    

    @coche.setter
    def coche(self, llantas):
        self._llantas = llantas
    def puerta (self, puerta):
        self._puerta = puerta
    def combustible (self, combustible):
        self._combustible = combustible
    def motor (self, motor):
        self._motor = motor

    
class Camioneta(Coche):
    def __init__(self,llantas,puerta,combustible,motor,modelo,marca_camioneta):
        super().__init__(llantas,puerta,combustible,motor)
        self._modelo = modelo
        self._marca_camioneta = marca_camioneta


class Motocicleta(Coche):
    def __init__(self, llantas, puerta, combustible, motor,cilindraje,marca_moto,asientos):
        super().__init__(llantas, puerta, combustible, motor)
        self._marca_moto = marca_moto
        self._asientos   = asientos

class CarroParticular(Coche):
    def __init__(self, llantas, puerta, combustible, motor, marca_carro, asientos_cuero):
        super().__init__(llantas, puerta, combustible, motor)
        self._marca_carro = marca_carro
        self._asientos_cuero = asientos_cuero
   
def classify_truck():
    renoleta = Camioneta(4,4,"Electrico",150,"2011","Renault Duster")
    renoleta.puerta = int(input("Ingrese el numero de puertas: "))
    renoleta.llantas= int(input("Ingrese el numero de llantas: "))
    renoleta.motor = int(input("Ingrese la capacidad del motor: "))
    renoleta.combustible = input("Ingrese el tipo de motor: ")
    renoleta.modelo = input ("Ingrese el modelo del vehículo: ")

    print("Puertas: "+str(renoleta.puerta))
    print("Llantas: "+str(renoleta.llantas))
    print("Motor: "+str(renoleta.motor))
    print("Tipo de combustible: "+renoleta.combustible)
    print("Modelo: "+renoleta.modelo)

def leather_seats(seats):
    if seats == 'si':
        return True
    elif seats == 'no':
        return False           

def classify_car():
    carro = CarroParticular(4,4,"Eléctrico",1500,"Chevrolet","no")
    carro.puerta = int(input("Ingrese el numero de puertas: "))
    carro.llantas= int(input("Ingrese el numero de llantas: "))
    carro.motor = int(input("Ingrese la capacidad del motor: "))
    carro.combustible = input("Ingrese el tipo de motor: ")
    carro.modelo = input ("Ingrese el modelo del vehículo: ")
    
    tiene_asientos = input("Tiene asientos de cuero: ")
    carro.asientos_cuero = leather_seats(tiene_asientos)
    
    if carro.asientos_cuero == True:
        print("Puertas: "+str(carro.puerta))
        print("Llantas: "+str(carro.llantas))
        print("Motor: "+str(carro.motor))
        print("Tipo de combustible: "+carro.combustible)
        print("Modelo: "+carro.modelo)
        print("El coche tiene asientos de cuero")
    else:
        print("Puertas: "+str(carro.puerta))
        print("Llantas: "+str(carro.llantas))
        print("Motor: "+str(carro.motor))
        print("Tipo de combustible: "+carro.combustible)
        print("Modelo: "+carro.modelo)
        print("El coche no tiene asientos de cuero")

    
    


def opcion():

    opciones = input("Ingrese una opción para ver: ")
    if opciones == 'a':
        return classify_truck()
    elif opciones == 'b':
        return classify_car()
    else:
        print("Unavailable option!")
    

if __name__ == '__main__':
    opcion()
    

