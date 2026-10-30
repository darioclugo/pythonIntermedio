from abc import ABC, abstractmethod

class cuentaBancaria(ABC):
    def __init__(self, titular, cbu, saldo_inicial=0.0):
        self.titular = titular       
        self._cbu = cbu              
        self._saldo = 0.0            
        self.saldo = saldo_inicial

    @property
    def cbu(self):
        return self._cbu

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("Error: El saldo no puede ser menor a cero.")
        self._saldo = valor

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor a cero.")
        self.saldo += monto
        print(f"Depósito exitoso de ${monto}. Nuevo saldo: ${self.saldo}")

    @abstractmethod
    def extraer(self, monto):
        pass

    def __str__(self):
        tipo = self.__class__.__name__.upper()
        return f"[{tipo}] TITULAR: {self.titular} | CBU: {self.cbu} | SALDO: ${self.saldo:.2f}"