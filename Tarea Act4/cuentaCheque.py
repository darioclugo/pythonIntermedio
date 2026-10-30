from cuentaBancaria import cuentaBancaria

class cuentaCheque(cuentaBancaria):
    def __init__(self, titular, cbu, saldo_inicial=0.0, costo_emision=50.0):
        super().__init__(titular, cbu, saldo_inicial)
        self.costo_emision = costo_emision

    def extraer(self, monto):
        if monto <= 0:
            raise ValueError("El monto a extraer debe ser mayor a cero.")
        total_a_descontar = monto + self.costo_emision
        if total_a_descontar > self.saldo:
            raise ValueError("Fondos insuficientes para cubrir el monto y la comisión por emisión.")
        self.saldo -= total_a_descontar
        print(f"Extracción de ${monto} con comisión de ${self.costo_emision}. Saldo actual: ${self.saldo}")