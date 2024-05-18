'''
Ejemplo: Encapsulamiento
Crear una clase Cuenta Bancaria que tenga las características titular y saldo encapsulado. De la
cuenta bancaria se puede obtener el saldo, depositar o retirar (en cada caso imprimir que fue
exitoso). Se debe crear la clase e implementarla.
'''
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.__titular = titular
        self.__saldo = saldo_inicial

    def obtener_saldo(self):
        return self.__saldo

    def depositar(self, cantidad):
        self.__saldo += cantidad
        print(f"Deposito exitoso. Nuevo saldo: {self.__saldo}")
    
    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo:{self.__saldo}")
        else:
            print("Fondos insuficientes.")

#creo cuenta bancaria
cuenta = CuentaBancaria("brian gomez", 10000)

#obtengo saldo
print("Saldo actual", cuenta.obtener_saldo())

#realizar opreciones de deposito y retiro
cuenta.depositar(1000)
cuenta.retirar(200)
cuenta.retirar(1500)