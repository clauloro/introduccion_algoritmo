def area_triangulo_rectangulo(base, altura):
  return (base * altura) / 2

base = float(input("Introduce la medida de la base: "))
altura = float(input("Introduce la medida de la altura: "))

area = area_triangulo_rectangulo(base, altura)

print("El área del triángulo rectángulo es:", area)
