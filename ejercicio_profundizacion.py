from ast import Import, Return
import sqlite3
import numpy as np
import matplotlib.pyplot as plt


def fetch():

    conn = sqlite3.connect('heart.db')
    c = conn.cursor()

    c.execute('SELECT pulso FROM sensor')
    data = c.fetchall()
    #print(data)

    return data

def show(data):

    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot(data, c='r', ls = '--')
    ax.legend('Pulso', fontsize= 10)
    ax.set_title('Evolución ritmo cardíaco')
    ax.set_facecolor('black')
    ax.grid('dashed')
    plt.show()

def estadistica(data):
    print('Calculando valores estadísticos extraidos de la tabla')
    print(     )
    valor_medio = np.mean(data).round(2)
    valor_min = np.mean(data).round(2)
    valor_max = np.mean(data).round(2)
    desvio_estandar = np.std(data).round(2)

    print('el valor medio es de', valor_medio)
    print('el valor máximo es de',valor_max)
    print('el valor mínimo es de',valor_min)
    print('la desviación estandar es de',desvio_estandar)


def regiones(data):
    valor_mean = np.mean(data)
    valor_std = np.std(data)

    x1 = []
    y1 = []
    x2 = []
    y2 = []
    x3 = []
    y3 = []

    for i in range(len(data)):
        if data[i] <= (valor_mean-valor_std):
            x1.append(i)
            y1.append(data[i])
        elif data[i] >= (valor_mean+valor_std):
            x2.append(i)
            y2.append(data[i])
        else:
            x3.append(i)
            y3.append(data[i])

    fig = plt.figure()
    fig.suptitle('Regiones del pulso', fontsize=15)
    ax = fig.add_subplot()

    ax.scatter(x1, y1, c='r', label='Aburrido')
    ax.scatter(x3, y3, c='g', label='Tranquilo')
    ax.scatter(x2, y2, c='b', label='Entusiasmado')
    ax.legend()
    ax.grid()
    plt.show()






if __name__ == "__main__":
  # Leer la DB
  data = fetch()

  # Data analytics
  show(data)
  estadistica(data)
  regiones(data)