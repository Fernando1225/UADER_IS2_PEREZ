#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys



# En el de extremos el factorial iba desde el extremo x hasta el extremo y
# Ahora modificado se calcula el factorial del valor ingresado y despues se calcula el factorial desde el valor ingresado
# hasta 60

class Factorial:

    def __init__(self, min, max):
        self.min = min
        self.max = max


    def run(self):
        min = self.min
        max = self.max

        factoriales = []
        min += 1 
        max -= 1 
        if (min < 0 or max < 0): 
            print("Factorial de un número negativo no existe")

        elif max == 0: 
            return 1
            
        else:
            num = min
            while(num <= max):
                min = num
                fact = 1
                while(min > 1):
                    fact *= min 
                    min -= 1
                num +=1
                factoriales.append(fact)
        return factoriales


if len(sys.argv) == 0:
    print("Debe informar un número!")
    sys.exit()

if (len(sys.argv) == 1):
    numeros = input('Ingrese numeros extremos! (ej: 4-8) ')
    numeros = numeros.split('-')
    num=int(numeros[0])
    num2 = int(numeros[1])

else:

    systemvar = sys.argv[1]
    systemvar = systemvar.split('-')

    num=int(systemvar[0])
    num2 = int(systemvar[1])

factorial = Factorial(num, num2)

factoriales = factorial.run()


print("Factoriales desde", num, "(no incluye) hasta", num2, "(no incluye) son:", factoriales)

# print("Factorial ",num,"! es ", factorial(num)) 

