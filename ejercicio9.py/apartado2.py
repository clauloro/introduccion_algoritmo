def calcular_media_ponderada(num1, pond1, num2, pond2, num3, pond3):
    media_ponderada = (num1 * pond1 + num2 * pond2 + num3 * pond3) / (pond1 + pond2 + pond3)
    return media_ponderada

num1 = float(input("Ingrese el primer número: "))
pond1 = float(input("Ingrese el coeficiente de ponderación para el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
pond2 = float(input("Ingrese el coeficiente de ponderación para el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
pond3 = float(input("Ingrese el coeficiente de ponderación para el tercer número: "))

media_ponderada = calcular_media_ponderada(num1, pond1, num2, pond2, num3, pond3)

print("La media ponderada es:", media_ponderada)
