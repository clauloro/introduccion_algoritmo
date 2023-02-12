def aplicar_impuestos(funcion):
    def wrapper(*args, **kwargs):
        precio_sin_impuestos = args[0]
        porcentaje_IVA = args[1]
        TII = precio_sin_impuestos * (1 + porcentaje_IVA/100)
        for i in range(2, len(args)):
            TII *= (1 + args[i]/100)
        return TII
    return wrapper

@aplicar_impuestos
def precio_TII(*args):
    pass

precio_sin_impuestos = float(input("Introduce el precio sin impuestos: "))
porcentaje_IVA = float(input("Introduce el porcentaje de IVA: "))
otros_impuestos = [float(impuesto) for impuesto in input("Introduce los otros impuestos separados por comas: ").split(',')]
args = [precio_sin_impuestos, porcentaje_IVA] + otros_impuestos

print("El precio con todos los impuestos incluidos es:", precio_TII(*args))
