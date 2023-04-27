from abc import ABC, abstractmethod

class TrenLaminador(ABC):
    @abstractmethod
    def producir_lamina(self, espesor, ancho):
        pass

class TrenLaminador5(TrenLaminador):
    def producir_lamina(self, espesor, ancho):
        print(f"Produciendo lamina de {espesor}'' de espesor y {ancho} mts de ancho en TrenLaminador5 (5 mts de largo).")
        
class TrenLaminador10(TrenLaminador):
    def producir_lamina(self, espesor, ancho):
        print(f"Produciendo lamina de {espesor}'' de espesor y {ancho} mts de ancho en TrenLaminador10 (10 mts de largo).")

class Lamina:
    def __init__(self, espesor, ancho, tren_laminador):
        self.espesor = espesor
        self.ancho = ancho
        self.tren_laminador = tren_laminador

    def producir(self):
        self.tren_laminador.producir_lamina(self.espesor, self.ancho)




tren_laminador_5 = TrenLaminador5()
tren_laminador_10 = TrenLaminador10()

lamina_5_mts = Lamina(0.5, 1.5, tren_laminador_5)
lamina_10_mts = Lamina(0.5, 1.5, tren_laminador_10)

# Producen las respectivas láminas de 0.5'' de espesor, 1.5 mts de ancho y 5 mts y 10 mts de largo
lamina_5_mts.producir()
lamina_10_mts.producir()