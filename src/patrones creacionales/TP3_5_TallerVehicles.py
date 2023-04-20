import os
#*--------------------------------------------------------------------
#* La clase Director orquesta la construcción del objeto indicando 
#* el orden en que deben llamarse sus componentes, los mismos son
#* genéricos y dependerán del builder específico utilizado sus
#* valores concretos
#*--------------------------------------------------------------------
class Director:
   __builder = None
   
   def setBuilder(self, builder):
      self.__builder = builder

   def getCar(self):
      car = Car()
      
      # Primero el chasis
      body = self.__builder.getBody()
      car.setBody(body)
      
      # Luego el motor
      engine = self.__builder.getEngine()
      car.setEngine(engine)
      
      # Finalmente (4) ruedas
      i = 0
      while i < 4:
         wheel = self.__builder.getWheel()
         car.attachWheel(wheel)
         i += 1

      # Retorna el vehiculo completo
      return car

   def getPlane(self):
      plane = Plane()

      #Primero el chasis
      body = self.__builder.getBody()
      plane.setBody(body)

      # Luego el motor
      engine = self.__builder.getEngine()
      plane.setEngine(engine)

      # Luego agregamos el tren de aterrizaje
      undercarriage = self.__builder.getUndercarriage()
      plane.setUndercarriage(undercarriage)

      # Agregamos alas (2) y turbinas (2)
      i = 0
      while i < 2:
         wings = self.__builder.getWings()
         plane.setWings(wings)
         turbine = self.__builder.getTurbine()
         plane.setTurbine(turbine)
         i += 1

      #Finalmente (6) ruedas
      i = 0
      while i < 6:
         wheel = self.__builder.getWheel()
         plane.attachWheel(wheel)
         i += 1

      # Retorna el vehiculo completo
      return plane

#*----------------------------------------------------------------
#* Esta es la definición de un objeto vehiculo inicializando 
#* todos sus atributos
#*----------------------------------------------------------------
class Car:
   def __init__(self):
      self.__wheels = list()
      self.__engine = None
      self.__body = None

   def setBody(self, body):
      self.__body = body

   def attachWheel(self, wheel):
      self.__wheels.append(wheel)

   def setEngine(self, engine):
      self.__engine = engine

   def specification(self):
      print ("chasis: %s" % (self.__body.shape))
      print ("planta motora: %d" % (self.__engine.horsepower))
      print ("ruedas: %d\'" % (self.__wheels[0].size))


class Plane:
   def __init__(self):
      self.__wheels = list()
      self.__engine = None
      self.__body = None
      self.__undercarriage = None
      self.__turbine = list()
      self.__wings = list()


   def setBody(self, body):
      self.__body = body

   def attachWheel(self, wheel):
      self.__wheels.append(wheel)

   def setEngine(self, engine):
      self.__engine = engine

   def setTurbine(self, turbine):
      self.__turbine.append(turbine)

   def setWings(self, wings):
      self.__wings.append(wings)

   def setUndercarriage(self, undercarriage):
      self.__undercarriage = undercarriage

   def specification(self):
      print ("chasis: %s" % (self.__body.shape))
      print ("planta motora: %d" % (self.__engine.horsepower))
      print ("ruedas: %d\'" % (self.__wheels[0].size))
      print("Turbinas: %d\'" % (self.__turbine[0].size))
      print("Alas: %d\'" % (self.__wings[0].size))
      print("tren de aterrizaje: %d\'" % (self.__undercarriage.size))

#*-----------------------------------------------------------------
#* Builder
#* Clase genérica que solo define la interfaz de los métodos que el
#* Builder específico tiene que implementar
#*-----------------------------------------------------------------
class Builder:
	
      def getWheel(self): pass
      def getEngine(self): pass
      def getBody(self): pass
      def getTurbine(self): pass
      def getWings(self): pass
      def getUndercarriage(self): pass

#*-----------------------------------------------------------------
#* Esta es la hoja de ruta para construir un Jeep
#* Establece instancias para tomar ruedas, motor y chasis
#* estableciendo las partes específicas que (en un Jeep) 
#* deben tener esas partes
#*-------------------------------------------------------
class JeepBuilder(Builder):
   
   def getWheel(self):
      wheel = Wheel()
      wheel.size = 22
      return wheel
   
   def getEngine(self):
      engine = Engine()
      engine.horsepower = 400
      return engine
   
   def getBody(self):
      body = Body()
      body.shape = "SUV"
      return body
      


class PlaneBuilder(Builder):
   
   def getWheel(self):
      wheel = Wheel()
      wheel.size = 14
      return wheel
   
   def getEngine(self):
      engine = Engine()
      engine.horsepower = 800
      return engine
   
   def getBody(self):
      body = Body()
      body.shape = 'Anotonov An-225 "Miriya"'
      return body

   def getTurbine(self):
      turbine = Turbine()  
      turbine.size = 120
      return turbine

   def getUndercarriage(self):
      undercarriage = Undercarriage()
      undercarriage.size = 50
      return undercarriage

   def getWings(self):
      wings = Wings()
      wings.size = 450
      return wings

#*----------------------------------------------------------------
#* Define partes genéricas para un vehiculo (sin inicializar)
#*----------------------------------------------------------------
class Wheel:
   size = None

class Engine:
   horsepower = None

class Body:
   shape = None

class Turbine:
   power = None

class Wings:
   size = None

class Undercarriage:
   size = None


#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
#* Esta es la estructura main()
#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
def main():

#*----------------------------------------------------------------
#* Instancia la clase que será el resultado y la que guiará el 
#* proceso de construcción
#*----------------------------------------------------------------
   jeepBuilder = JeepBuilder() # initializing the class
   director = Director()
   planeBuilder = PlaneBuilder() # initializing the class
   director2 = Director()

#*----------------------------------------------------------------
#* Pasa al director la hoja de ruta para construir un Jeep
#*----------------------------------------------------------------   
   director.setBuilder(jeepBuilder)
   director2.setBuilder(planeBuilder)

#*----------------------------------------------------------------
#* Ordena al director agregar los componentes de un Jeep según
#* la hoja de ruta
#*----------------------------------------------------------------
   jeep = director.getCar()
   plane = director2.getPlane()

#*---------------------------------------------------------------
#* Finalizada la construcción verifica que sea completa
#*---------------------------------------------------------------
   print("Jeep")
   jeep.specification()
   print ("\n\n")

   print()

   print("Airplane")
   plane.specification()
   print ("\n\n")

#*----------------------------------------------------------------------
#* Se detecta el entry point y se lo deriva a una sección main() propia
#*----------------------------------------------------------------------
if __name__ == "__main__":
   os.system("clear")
   print("Ejemplo de un patrón de tipo builder aplicado a la construcción de un vehículo\n")

   main()
