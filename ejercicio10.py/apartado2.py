def area_triangulo_rectangulo_decorador(func):
    def wrapper(base, altura):
        result = func(base, altura)
        return result
    return wrapper

@area_triangulo_rectangulo_decorador
def area_triangulo_rectangulo(base, altura):
    return (base * altura) / 2

base = float(input("Ingrese la medida de la base: "))
altura = float(input("Ingrese la medida de la altura: "))
resultado = area_triangulo_rectangulo(base, altura)
print("El área del triángulo rectángulo es:", resultado)
