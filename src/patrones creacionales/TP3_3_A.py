from abc import ABC, abstractmethod

class Hamburguesa(ABC):
    @abstractmethod
    def entrega(self):
        pass

class HamburguesaMostrador(Hamburguesa):
    def entrega(self):
        print("La hamburguesa está lista para ser retirada en el mostrador.")

class HamburguesaRetirada(Hamburguesa):
    def entrega(self):
        print("La hamburguesa está lista para ser retirada por el cliente.")

class HamburguesaDelivery(Hamburguesa):
    def entrega(self):
        print("La hamburguesa está lista para ser enviada por delivery.")

class HamburguesaFactory:
    def __init__(self, entrega):
        self.entrega = entrega
    
    def crear_hamburguesa(self):
        if self.entrega == "mostrador":
            return HamburguesaMostrador()
        elif self.entrega == "retirada":
            return HamburguesaRetirada()
        elif self.entrega == "delivery":
            return HamburguesaDelivery()
        else:
            raise ValueError("Tipo de entrega no válido.")



print("Hamburguesa 1:")
factory = HamburguesaFactory("mostrador")
hamburguesa = factory.crear_hamburguesa()
# Print el tipo de entrega de la hamburguesa
hamburguesa.entrega()  

print()
print("Hamburguesa 2:")
factory = HamburguesaFactory("delivery")
hamburguesa = factory.crear_hamburguesa()
# Print el tipo de entrega de la hamburguesa
hamburguesa.entrega()  
