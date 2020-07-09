import matplotlib.pyplot as plt
from math import *
import numpy as np

plt.style.use("ggplot")

#variaveis
global x_in, tau, t, tf
steps = [0.1, 0.5]
tf = 6
x_in = 10.
tau = 2.

#analitica
ta = np.arange(0, tf, 0.0001)
xa = x_in * np.exp(-ta/tau)

#funcoes
def plot(step, plot_x, plot_y, met): #plot_x e plot_y sao listas
    for i in range(len(step)):
        plt.plot(plot_x[i], plot_y[i], label=str(step[i]) +" "+ met)
    

    
def time(dt, t):
    tind = []
    while (t<=tf):
        tind.append(t)
        t = t+dt
    
    return tind



def midpoint(dt, x):
    ind = []
    t=0
    while (t<=tf):
        ind.append(x)
        k1 = -(x/tau)
        x_aux = x + (1./2.)*k1*dt
        k2 = -(x_aux/tau)
        x = x + k2*dt
        t = t+dt
        
    return ind



def rk4_3o8(dt, x):
    ind = []
    t=0
    while (t<=tf):
        ind.append(x)
        k1 = -(x/tau)
        k2 = -(x + k1*(dt/3.))/tau
        k3 = -(x - k1*(dt/3.) + k2*dt)/tau
        k4 = -(x + k1*dt - k2*dt + k3*dt)/tau
        x = x + (1./8.)*(k1 + 3.*k2 + 3.*k3 + k4)*dt
        t = t+dt
        
    return ind
        


def rk4_classic(dt, x):
    ind = []
    t=0
    while (t<=tf):
        ind.append(x)
        k1 = -(x/tau)
        k2 = -(x + (1./2.)*k1*dt)/tau
        k3 = -(x + (1./2.)*k2*dt)/tau
        k4 = -(x + k3*dt)/tau
        x = x + (1./6.)*(k1 + 2.*k2 + 2.*k3 + k4)*dt
        t = t+dt
        
    return ind



#aplicacao
#rk4 classic
rk4_plot = [rk4_classic(dt, x_in) for dt in steps]
    
#rk4 3/8
rk4_3o8 = [rk4_3o8(dt, x_in) for dt in steps]

#plots
t_plot = [time(dt, t=0) for dt in steps]    
midpoint_plot = [midpoint(dt, x_in) for dt in steps]

plt.plot(ta, xa, label="analitica", c="black")
plot(steps, t_plot, midpoint_plot, met="pm")
plot(steps, t_plot, rk4_plot, met="rk4")

plt.xlabel("Tempo")
plt.ylabel("Num. de atomos")
plt.legend()
plt.show()


for el in range(len(steps)):
    print("RK4 3/8 para o passo " + str(steps[el]) + ":")
    print(rk4_3o8[el], "\n")
