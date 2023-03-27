#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    factoriales = []
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

        factoriales.append(fact)

        fact = 60
        num = num3
        while (num <= 60):
            fact *= num
            num +=1
        factoriales.append(fact)

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

