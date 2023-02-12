def calcular_horas_extra(funcion):
    def wrapper(salario_mensual, horas_extra):
        tarifa_hora = salario_mensual / (35 * 52) / 12
        horas_normales = 8
        horas_pagadas = horas_normales + horas_extra
        
        if horas_extra <= 8:
            return funcion(tarifa_hora, horas_extra)
        elif horas_extra > 8 and horas_extra <= 36:
            return funcion(tarifa_hora, horas_extra) + (tarifa_hora * 0.25 * (horas_extra - 8))
        elif horas_extra > 36 and horas_extra <= 43:
            return funcion(tarifa_hora, horas_extra) + (tarifa_hora * 0.25 * 28) + (tarifa_hora * 0.5 * (horas_extra - 36))
        elif horas_extra > 43:
            return funcion(tarifa_hora, horas_extra) + (tarifa_hora * 0.25 * 28) + (tarifa_hora * 0.5 * 7) + (tarifa_hora * 0.75 * (horas_extra - 43))
        
    return wrapper

@calcular_horas_extra
def horas_pagadas(tarifa_hora, horas_extra):
    return tarifa_hora * horas_extra

