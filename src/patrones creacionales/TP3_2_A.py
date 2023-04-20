class CalculadoraImpuestos:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def calcular_impuestos(self, base_imponible):
        iva = base_imponible * 0.21
        iibb = base_imponible * 0.05
        contrib_mun = base_imponible * 0.012
        total_impuestos = iva + iibb + contrib_mun
        return total_impuestos



calc_impuestos = CalculadoraImpuestos()

user_input = int(input("Ingrese monto para calcular impuestos: $"))

monto = calc_impuestos.calcular_impuestos(user_input)


print(f"Total de impuesto a pagar: ${monto}")
print(f"Total del monto mas impuestos: ${user_input+monto}")