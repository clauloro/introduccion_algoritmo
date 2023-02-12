def calcular_media_aritmética(num1, num2, num3):
    media_aritmetica = (num1 + num2 + num3) / 3
    return media_aritmetica

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

media_aritmetica = calcular_media_aritmética(num1, num2, num3)

print("La media aritmética es:", media_aritmetica)
