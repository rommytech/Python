# -*- coding: utf-8 -*-

class CuentaGalactica:
    def __init__(self):
        self.saldo = 0

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito exitoso de {monto} créditos galácticos. Saldo actual: {self.saldo}")
        else:
            print("El monto debe ser mayor que cero.")

    def retirar(self, monto):
        if monto > 0 and self.saldo >= monto:
            self.saldo -= monto
            print(f"Retiro exitoso de {monto} créditos galácticos. Saldo actual: {self.saldo}")
        else:
            print(f"Fondos insuficientes o monto inválido. Saldo actual: {self.saldo}")
