# import sys
import matplotlib.pyplot as plt
#No imorta el valor del num, siempre termina en 4 2 1.
def calcularNCollatz(num):
    cant_iter = 1
    iteracciones = [num]
    while (num != 1):
        if (num % 2 == 0):
            num = int(num / 2)
        else:
            num = (num*3) + 1
        
        cant_iter += 1
        iteracciones.append(num)
    valores = [num, cant_iter, iteracciones]
    return valores

x = []
y = []
for i in range(1,10000):
    a = calcularNCollatz(i)[2]
    x.append(i)
    y.append(len(a))
plt.plot(x, y, "o")
plt.show()
# if len(sys.argv) == 0:
#     print("Debe informar un número!")
#     sys.exit()
# if (len(sys.argv) == 1):
#     numeros = input('Ingrese un numero! ')
#     num=int(numeros[0])
# else:
#     num = int(sys.argv[1])
# print("Se necesitaron estas iteracciones", calcularNCollatz(num)[2],"para el numero",num)
# nCollatz = calcularNCollatz(num)
# print(nCollatz[1])
# plt.plot(nCollatz[0], nCollatz[1])
# plt.show()