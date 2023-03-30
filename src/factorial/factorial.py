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

def factorial(num): 
    factoriales = []
    factoriales_hasta = []
    factoriales_desde = []
    if num < 0: 
        print("Factorial de un número negativo no existe")

    elif num == 0: 
        return 1
        
    else:
        num3 = num
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1

            factoriales_hasta.append(fact)

        fact = num3
        num = num3
        num +=1
        while (num < 60):
            fact *= num
            num +=1
            factoriales_desde.append(fact)

    factoriales.append(factoriales_hasta)
    factoriales.append(factoriales_desde)

    return factoriales


if len(sys.argv) == 0:
    print("Debe informar un número!")
    sys.exit()

if (len(sys.argv) == 1):
    num = int(input('Ingrese un numero! '))
else:
    num=int(sys.argv[1])


print("Factorial -hasta ",num,"! es ", factorial(num)[0]) 
print("Factorial desde- ",num,"! hasta 60 es ", factorial(num)[1])

# print("Factorial ",num,"! es ", factorial(num)) 

