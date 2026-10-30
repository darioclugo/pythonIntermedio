from abc import ABC 
from cuentaBancaria import cuentaBancaria

class cuentaAhorro(cuentaBancaria):
    def extraer(self, monto):
        if monto <= 0:
            raise ValueError("El monto a extraer debe ser mayor a cero.")
        if monto > self.saldo:
            raise ValueError("Fondos insuficientes en la Cuenta de Ahorro.")
        self.saldo -= monto
        print(f"Extracción de ${monto} exitosa. Saldo restante: ${self.saldo}")

    def aplicar_interes(self):
        tasa = 0.001
        interes = self.saldo * tasa
        self.saldo += interes
        print(f"Interés aplicado (${interes:.2f}). Nuevo saldo: ${self.saldo:.2f}")