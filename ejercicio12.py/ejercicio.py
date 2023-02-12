class Cuenta:
    def __init__(self, nombre, saldo, descubierto_permitido):
        self.nombre = nombre
        self.saldo = saldo
        self.descubierto_permitido = descubierto_permitido

    def retirar(self, cantidad):
        if self.saldo - cantidad >= -self.descubierto_permitido:
            self.saldo -= cantidad
            print("Retirada exitosa")
        else:
            print("Saldo insuficiente")
    
    def depositar(self, cantidad):
        self.saldo += cantidad
        print("Depósito exitoso")
        
    def ver_saldo(self):
        print("Saldo actual:", self.saldo)
