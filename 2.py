import matplotlib.pyplot as plt
import numpy as np
import time

def collatz_sequence(numero, ax):
    secuencia = [numero]
    while numero != 1:
        if numero % 2 == 0:
            numero = numero / 2
        else:
            numero = numero * 3 + 1
        secuencia.append(numero)
        print(numero)  # Imprime el número actual de la secuencia
        time.sleep(0.5)  # Retrasa por 0.5 segundos
        ax.plot(len(secuencia)-1, numero, 'ro')  # Agrega un punto rojo a la gráfica
        plt.pause(0.001)  # Actualiza la gráfica en tiempo real
    return secuencia

numero = int(input("Ingrese el número: "))

fig, ax = plt.subplots()
ax.plot([], [])

secuencia = collatz_sequence(numero, ax)

x = np.arange(len(secuencia))
y = np.array(secuencia)

ax.plot(x, y, 'b-')

for i, valor in enumerate(secuencia):
    ax.annotate(str(valor), (x[i], y[i]))

ax.plot(len(secuencia)-1, numero, 'ro')  # Agrega un punto rojo a la gráfica

ax.set(xlabel='Paso', ylabel='Número',
       title='Secuencia de Collatz para {}'.format(numero))
ax.grid()

plt.show()



