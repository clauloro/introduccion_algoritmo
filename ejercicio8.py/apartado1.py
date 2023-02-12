def calcular_impuesto(cantidad, IVA):
    return cantidad * (IVA / 100)

def calcular_precio_total(cantidad, IVA):
    vat = calcular_impuesto(cantidad, IVA)
    return cantidad + IVA

cantidad = 100
IVA = 21

calcular_precio_total = calcular_precio_total(cantidad, IVA)

print(f"Cantidad: {cantidad}")
print(f"VAT ({IVA}%): ${calcular_impuesto(cantidad, IVA):.2f}")
print(f"Precio total: {calcular_precio_total:.2f}")
