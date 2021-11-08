
# Dario Castillo - 2021
# Foro de dabe: Calculo diferencial.
# Funcion que calcula el daño
# de un personaje en un videojuego.

# importamos las librerias necesarias
# numpy nos permitemanejar arrays de manera mas  limpia
# matpltlib nos permite graficar funciones

import numpy as np
from matplotlib import pyplot as plt

# la variable x represneta los niveles del personaje
# con el metodo arange() de numpy podemos definir la cantidad
# de niveles que deseamos, en este caso 80

x = np.arange(80)

# creamos la funcion como tal, con los valores fijos
# y reciviendo como parametro los valores variables.

def f(x):
    return ( ( (5 + (x*2) )  ) ** 2 ) * 0.01

# usamos el metodo plot de matplotlib para mostrar en pantalla
# la funcion graficada, esta recine por parametros, la variable
# y la funcion que se aplica sobre dicha variable

plt.plot(x, f(x))
plt.xlabel('Nivel')
plt.ylabel('Daños realizado')
plt.grid()
plt.show()