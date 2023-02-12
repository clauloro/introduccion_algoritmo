def deco_media(func):
    def wrapper(*args):
        return sum(args) / len(args)
    return wrapper

@deco_media
def media(*args):
    pass

resultado = media(1, 2, 3)
print(resultado) 

