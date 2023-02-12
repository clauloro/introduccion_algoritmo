def calcular_horas_extra(salario_mensual, horas_extra):
    tarifa_hora = salario_mensual / (52 * 35)
    if horas_extra <= 43:
        tarifa_extra = tarifa_hora * 1.25
    else:
        tarifa_extra = tarifa_hora * 1.50
    pago_horas_extra = tarifa_extra * horas_extra
    return pago_horas_extra

salario_mensual = float(input("Introduce el salario mensual bruto: "))
horas_extra = float(input("Introduce el número de horas extra: "))
pago_horas_extra = calcular_horas_extra(salario_mensual, horas_extra)
print("El pago por horas extra es de:", pago_horas_extra)
