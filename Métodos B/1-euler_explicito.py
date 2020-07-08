import matplotlib.pyplot as plt
from math import *
import numpy as np

plt.style.use("ggplot")

x_in = float(input("valor de x inicial: "))
tf = float(input("valor final de tempo: "))
tau = 2.
delta = [0.01, 0.1, 0.5, 1., 2.]

t = 0.

tplot = []
xplot = []

tind = []
xind = []

x = x_in
x_loop = x_in
t_loop = t

ta = np.arange(0, tf, 0.01)
xa = x * np.exp(-ta/tau)

for passo in delta:
    while t <= tf:
        x = x - (x/tau)*passo
        tind.append(t)
        xind.append(x)
        t = t + passo
    
    t = 0.
    x = x_in	
    tplot.append(tind)
    xplot.append(xind)
    xind = []
    tind = []
    
    print("\nValor do passo: ", str(passo))
    print("5 primeiros valores (t, x): ")
    for i in range(5):
        x_loop = x_loop - (x_loop/tau)*passo
        print(t_loop, x_loop)
        t_loop = t_loop + passo

    x_loop = x_in
    t_loop = 0.
        

for j in (range(len(delta))):
    plt.plot(tplot[j], xplot[j], label=str(delta[j]))

plt.plot(ta, xa, label="analitica", c="black")
    
plt.xlabel("Tempo")
plt.ylabel("Numero de atomos")
plt.legend()
plt.show()
