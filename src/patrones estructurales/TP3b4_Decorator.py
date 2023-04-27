class Numero:
    def __init__(self, valor):
        self.valor = valor
    
    def imprimir(self):
        print("Número:", self.valor)
        
class Operacion:
    def __init__(self, operacion):
        self.operacion = operacion
        
    def imprimir(self):
        self.operacion.imprimir()
        
    def sumar(self):
        self.operacion.valor += 2
        return self.operacion
        
    def multiplicar(self):
        self.operacion.valor *= 2
        return self.operacion
        
    def dividir(self):
        self.operacion.valor /= 3
        return self.operacion


numero = int(input('Ingrese un numero: '))

numero = Numero(numero)
# Print num
numero.imprimir()

numero = Operacion(numero).sumar()
# Print num + 2
numero.imprimir()

numero = Operacion(numero).multiplicar()
# Print num 1* 2
numero.imprimir()

numero = Operacion(numero).dividir()
# Print num / 3
numero.imprimir()



