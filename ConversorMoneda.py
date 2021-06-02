def exchange():
    valor_pesos = int(input("Ingrese el valor en pesos colombianos: ")) 

    COPtoUSD = valor_pesos/(2700)
    COPtoEUR = valor_pesos/(2200)

    print("Valor en COP: "+str(valor_pesos))
    print("Dinero en dólares americanos: "+str(float(COPtoUSD)))
    print("Dinero en euros: "+str(float(COPtoEUR)))

if __name__ == '__main__':
    exchange()