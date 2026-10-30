from cuentaBancaria import cuentaBancaria

class cuentaCorriente(cuentaBancaria):
    def __init__(self, titular, cbu, saldo_inicial=0.0, limite_descubierto=500.0):
        super().__init__(titular, cbu, saldo_inicial)
        self.limite_descubierto = limite_descubierto

    def extraer(self, monto):
        if monto <= 0:
            raise ValueError("El monto a extraer debe ser mayor a cero.")
        if monto > (self.saldo + self.limite_descubierto):
            raise ValueError("La extracción supera el saldo y el límite descubierto permitido.")
        
        # Modificamos directamente _saldo para permitir valores negativos
        self._saldo -= monto
        print(f"Extracción de ${monto} exitosa. Saldo actual: ${self._saldo}")