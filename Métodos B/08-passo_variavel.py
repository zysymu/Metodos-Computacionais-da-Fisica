import time
from math import *
import matplotlib.pyplot as plt

plt.style.use("ggplot")

#definindo variaveis
global tf, a, lim_sup
tolerance = 1e-4
dt_in = 1e-5
x_in = 0.001
a = 0.1
lim_sup = 2. 
tf = 100

#definindo funcoes
def rk2(dt, x):
    k1 = a*x*(2 - x)
    x_aux = x + (1./2.)*k1*dt
    k2 = a*x_aux*(2 - x_aux)
    x = x + k2*dt
        
    return x


def rk4(dt, x):
    k1 = a*x*(2 - x)
    k2 = a*x*(2 - (x + (1./2.)*k1*dt))
    k3 = a*x*(2 - (x + (1./2.)*k2*dt))
    k4 = a*x*(2 - (x + k3*dt))
    x = x + (1./6.)*(k1 + 2.*k2 + 2.*k3 + k4)*dt
        
    return x



#algoritmo
val_tsys = []
val_m = []
for m in range(1,100):
    n = 0
    t = 0.
    start_time = time.time()
    plot_x = []
    plot_t = []

    x = x_in
    dt = dt_in


    while (t<=tf):
        x_aux = x
        n = n+1
        x_rk2 = rk2(dt, x)  
        x = rk4(dt, x)
            
        if n%m == 0: #isso eh a correcao pro delta_t
            current_error = sqrt(abs( ((x - x_aux)**2) - ((x_rk2 - x_aux)**2) ))
            dt_new = dt * ((tolerance/current_error)**(1/3))

            if dt_new > 2*dt:
                dt_new = 2*dt
                dt = dt_new

            else:
                dt = dt_new

        plot_t.append(t)
        plot_x.append(x)
        t = t+dt

    dif_time = time.time() - start_time
    val_tsys.append(dif_time)
    val_m.append(m)


#print(plot_x)
#fazer um sort na lista depois e encontrar o elemento que tem menor tempo de execucao
shortest = [i[0] for i in sorted(enumerate(val_tsys), key=lambda x:x[1])][0]
shortest_m = val_m[shortest]
print(f"o m que minimiza o tempo eh {shortest_m}, levando um tempo de {val_tsys[shortest]} para rodar o programa, com um erro de {current_error}")

plt.plot(plot_t, plot_x)
plt.show()
