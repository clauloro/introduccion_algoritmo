def area_triangulo(lado, altura):
  return (lado * altura) / 2

lado = float(input("Introduce la medida del lado: "))
altura = float(input("Introduce la medida de la altura: "))

resultado = area_triangulo(lado, altura)
print("El área del triángulo es:", resultado)
