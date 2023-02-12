def media_ponderada_decorador(func):
    def wrapper(*args, **kwargs):
        pesos = kwargs['pesos']
        numeros = args
        total = 0
        for i in range(len(numeros)):
            total += numeros[i] * pesos[i]
        result = total / sum(pesos)
        return result
    return wrapper

@media_ponderada_decorador
def media_ponderada(*args, **kwargs):
    pass

numeros = [3, 5, 7]
pesos = [2, 3, 4]
resultado = media_ponderada(*numeros, pesos=pesos)
print("La media ponderada es: ", resultado)

