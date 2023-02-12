def intereses(func):
    def wrapper(*args, **kwargs):
        capital, tasa, tiempo = args
        interes = capital * tasa * tiempo / 12
        result = func(interes)
        return result
    return wrapper

@intereses
def calc_intereses(interes):
    return interes
