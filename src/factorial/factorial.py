#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num, num2): 
    factoriales = []
    if (num < 0 or num2 < 0): 
        print("Factorial de un número negativo no existe")

    elif num2 == 0: 
        return 1
        
    else:
        num3 = num
        while(num3<=num2):
            num = num3
            fact = 1
            while(num > 1): 
                fact *= num 
                num -= 1
            num3 += 1
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


print("Factoriales desde", num, " hasta", num2, " son:", factorial(num, num2))

# print("Factorial ",num,"! es ", factorial(num)) 

