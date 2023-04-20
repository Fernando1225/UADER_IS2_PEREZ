class Factura:
    def __init__(self, importe):
        self.importe = importe

    def calcular_total(self):
        return self.importe + (self.importe * self.calcular_iva())

    def crear_factura(importe, tipo_cliente):
        if tipo_cliente == "IVA Responsable":
            return FacturaIVAResponsable(importe)
        elif tipo_cliente == "IVA No Inscripto":
            return FacturaIVANoInscripto(importe)
        elif tipo_cliente == "IVA Exento":
            return FacturaIVAExento(importe)
        else:
            raise ValueError("Tipo de cliente desconocido")

class FacturaIVAResponsable(Factura):
    def calcular_iva(self):
        return 0.21

class FacturaIVANoInscripto(Factura):
    def calcular_iva(self):
        return 0.27

class FacturaIVAExento(Factura):
    def calcular_iva(self):
        return 0.105

print("Factura 1:")
factura = Factura.crear_factura(100, "IVA Responsable")
total = factura.calcular_total()
print(f"Factura mas iva agregado: ${total}")

print()
print("Factura 2:")
factura = Factura.crear_factura(100, "IVA Exento")
total = factura.calcular_total()
print(f"Factura mas iva agregado: ${total}")
