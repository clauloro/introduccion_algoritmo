def area_triangulo_decorador(funcion):
    def wrapper(*args, **kwargs):
        base = args[0]
        altura = args[1]
        resultado = (base * altura) / 2
        return resultado
    return wrapper

@area_triangulo_decorador
def area_triangulo(base, altura):
    pass

base = float(input("Introduce la medida de la base: "))
altura = float(input("Introduce la medida de la altura: "))
resultado = area_triangulo(base, altura)
print("El área del triángulo es:", resultado)

