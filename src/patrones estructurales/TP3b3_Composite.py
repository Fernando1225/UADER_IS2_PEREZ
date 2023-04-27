from abc import ABC, abstractmethod

class Componente(ABC):
    def operacion(self):
        pass

class Subconjunto(Componente):
    def __init__(self):
        self.componentes = []

    def add_componente(self, componente):
        self.componentes.append(componente)

    def remove_componente(self, componente):
        self.componentes.remove(componente)

    def operacion(self):
        for componente in self.componentes:
            componente.operacion()

class Pieza(Componente):
    def operacion(self):
        print("Realizando operación en una pieza.")

# Se crea el producto principal
prod_principal = Subconjunto()

# Creamos los tres subconjuntos
subconjunto_1 = Subconjunto()
subconjunto_2 = Subconjunto()
subconjunto_3 = Subconjunto()

# Se agregan cuatro piezas a cada subconjunto
for _ in range(4):
    subconjunto_1.add_componente(Pieza())
    subconjunto_2.add_componente(Pieza())
    subconjunto_3.add_componente(Pieza())

# Se agregan los subconjuntos al producto principal
prod_principal.add_componente(subconjunto_1)
prod_principal.add_componente(subconjunto_2)
prod_principal.add_componente(subconjunto_3)

# Se crea el optional_subset y se le agregan cuatro piezas mas
subconj_opcional = Subconjunto()
for _ in range(4):
    subconj_opcional.add_componente(Pieza())

# Se aggrega el optional_subset al producto principal
prod_principal.add_componente(subconj_opcional)

# Se realizan las operaciones en el main product
prod_principal.operacion()
