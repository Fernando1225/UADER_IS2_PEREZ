from abc import ABC, abstractmethod

class Hamburguesa(ABC):
    @abstractmethod

    def tipo_entrega(self):
        pass

class HamburguesaMostrador(Hamburguesa):
    def tipo_entrega(self):
        print("La hamburguesa está lista para ser retirada en el mostrador.")

class HamburguesaRetirada(Hamburguesa):
    def tipo_entrega(self):
        print("La hamburguesa está lista para ser retirada por el cliente.")

class HamburguesaDelivery(Hamburguesa):
    def tipo_entrega(self):
        print("La hamburguesa está lista para ser enviada por delivery.")

class HamburguesaFactory:
    def __init__(self, tipo_entrega):
        self.tipo_entrega = tipo_entrega
    
    def crear_hamburguesa(self):
        if self.tipo_entrega == "mostrador":
            return HamburguesaMostrador()
        elif self.tipo_entrega == "retirada":
            return HamburguesaRetirada()
        elif self.tipo_entrega == "delivery":
            return HamburguesaDelivery()
        else:
            raise ValueError("Tipo de entrega no válido.")



print("Hamburguesa 1:")
factory = HamburguesaFactory("mostrador")
hamburguesa = factory.crear_hamburguesa()
# Print el tipo de entrega de la hamburguesa
hamburguesa.tipo_entrega()  

print()
print("Hamburguesa 2:")
factory = HamburguesaFactory("delivery")
hamburguesa = factory.crear_hamburguesa()
# Print el tipo de entrega de la hamburguesa
hamburguesa.tipo_entrega()  
