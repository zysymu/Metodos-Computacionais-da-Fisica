#histo
import matplotlib.pyplot as plt
import numpy as np
plt.style.use("ggplot")

def pseudo(x):
    q = 127773
    r = 2836
    a = 16807
    b = 0
    M = 2147483544

    x = a*(x%q) - r*(x//q)
    if x < 0:
        x = x + M
    #print(x)
    return x

#entradas
def histo():
    N = [100, 1000, 10000] # numero de valores aleatorios que serao contados
    M = 100 # bins (numeros de particoes)
    L = 100 # tamanho do intervalo

    bigx = [] #contem todos os valores aleatorios que sao criados

    for amount in N:
        h = [0]*L # espacos que vao contar os numeros aleatorios
        x = 26514

        for t in range(amount):
            x = pseudo(x)
            bigx.append(x)
            s = x%L
            h[s] += 1
        #print(h)

        med = np.average(h)
        std = np.std(h)

        plt.plot(h)
        plt.axhline(med, c="b", label="media h")
        plt.axhspan((med-std), (med+std), color="green", alpha=0.5)
        plt.legend(loc="upper left")
        plt.title("N = " + str(amount))
        plt.show()
    
        print("fim \n")

    print(np.average(bigx))
    print(np.std(bigx))

histo()






