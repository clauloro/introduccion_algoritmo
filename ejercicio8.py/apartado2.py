def calcular_interes(capital, tasa, meses):
    interes = capital * tasa * meses / 12
    return interes

capital = float(input("Ingrese el capital invertido: "))
tasa = float(input("Ingrese la tasa de interés: ")) / 100
meses = int(input("Ingrese el tiempo de inversión en meses: "))

interes = calcular_interes(capital, tasa, meses)

print("El importe de los intereses es:", interes)
